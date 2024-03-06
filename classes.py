
import os
import time
import requests
from time import sleep
from predict_with_seps import change_cmyk_rgb, prediction, tile
from PySide6.QtCore import QThread, Signal, Slot, QTimer, QTime

class Thread_tg(QThread):
    ''' Класс отправки сообщений в Телеграмм '''

    def __init__(
        self,
        img_tg_check: str,
        bot_num: str,
        chat_id: str,
    ) -> None:
        super().__init__()
        self.img_tg_check = img_tg_check
        self.bot_num = bot_num
        self.chat_id = chat_id

    @Slot()
    def run(self):
        '''Реализация отправки сообщения в ТГ'''

        self.data = self.send_current_model_box(self.data)
        self.tg_is_running = True
        while self.tg_is_running:
            try:
                self.check_tg = os.listdir(self.img_tg_check)
                if self.check_tg:
                    self.send_tg = self.send_telegram(
                        self.data,
                        bot_num=self.bot_num,
                        chat_id=self.chat_id,
                        photo_path=(
                            self.img_tg_check + os.listdir(self.img_tg_check)[0]
                        ),
                    )
                    os.remove(
                        (self.img_tg_check + os.listdir(self.img_tg_check)[0])
                    )

            except FileNotFoundError:
                pass

    def send_telegram(self, 
        data: str, 
        bot_num: str, 
        chat_id: str, 
        photo_path: str) -> None:
        '''Функция отправки сообщения в ТГ'''

        bot_url = "https://api.telegram.org/bot" + bot_num + "/sendPhoto"
        time_tg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data_send = data + ' ' + time_tg
        payload = {"chat_id": chat_id, "caption": data_send}

        with open(photo_path, "rb") as image_file:
            send_photo_tg = requests.post(
                url=bot_url,
                data=payload,
                files={"photo": image_file},
            )

    def stop(self) -> None:
        ''' Остановить Thread'''

        self.tg_is_running = False

    def send_current_model_box(self, data: str) -> str:
        '''Получение имени текущей модели извне'''

        self.data = data
        return self.data

class Thread(QThread):
    '''Класс Thread для основного действия: смена цвета CMYK-RGB и инференс модели предсказания'''

    result_defect = Signal(str)
    result_norm = Signal(str)
    text = Signal(str)
    result_no_data = Signal(str)

    def __init__(
        self,
        camera_path: str,
        check_path: str,
        file_path: str,
        result_path_ok: str,
        result_path_defect: str,
        model_path: str,
        path_for_tg: str,
    ) -> None:
        super().__init__()
        self.camera_path = camera_path
        self.check_path = check_path
        self.file_path = file_path
        self.result_path_ok = result_path_ok
        self.result_path_defect = result_path_defect
        self.model_path = model_path
        self.path_for_tg = path_for_tg

    @Slot()
    def run(self):
        '''Запуск методов класса'''

        self.data = self.send_current_model_box(self.data)
        self.is_running = True

        while self.is_running:
            try:
                self.change_cmyk = change_cmyk_rgb(
                    change_img_path=self.camera_path, 
                    file_path=self.file_path,
                )
                self.img_check = os.listdir(self.check_path)
                if self.img_check:
                    self.signal_text, self.img_source_def, self.img_source_ok = prediction(
                        data=self.data,
                        file_path=self.file_path,
                        model_path=self.model_path,
                        result_path_ok=self.result_path_ok,
                        result_path_defect=self.result_path_defect,
                        path_for_tg=self.path_for_tg,
                    )

                    if self.signal_text:
                        self.signal_text = "НОРМА"
                        self.text.emit(self.signal_text)
                        self.result_norm.emit(self.img_source_ok)                                
                    else:
                        self.signal_text = "БРАК"
                        self.text.emit(self.signal_text)
                        self.result_defect.emit(self.img_source_def)

                    # self.result_norm.emit(self.signal_text)
                    # self.result_defect.emit(self.signal_text)


                    sleep(0.5)
                else:
                    self.result_no_data.emit("Нет данных!")
            except TypeError:
                pass

    def send_current_model_box(self, data: str):
        '''Получение имени текущей модели извне'''

        self.data = data
        return self.data

    def stop(self):
        ''' Остановить Thread'''

        self.is_running = False