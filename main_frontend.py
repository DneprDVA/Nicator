import os
import sys
from time import sleep
from PIL import Image
import shutil
import telepot
import requests
import pidfile

from predict import change_cmyk_rgb, prediction

from PySide6.QtCore import QThread, Signal, Slot, QTimer
from PySide6.QtGui import QPixmap, QIcon, QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar
from MainWindow import Ui_MainWindow
from style_sheet import (
    normal_button_state,
    green_button_state,
    bg_signal_norm,
    bg_sinal_defect,
    bg_signal_no_data,
)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = "QC-Monitoring"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


try:
    with pidfile.PIDFile("example.pid"):
        "Starting program execution"        

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
                payload = {"chat_id": chat_id, "caption": data}

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


                            sleep(1)
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

            

        class MyWindow(QMainWindow, Ui_MainWindow):
            def __init__(self, *args, obj=None, **kwargs):
                super(MyWindow, self).__init__(*args, **kwargs)
                self.setupUi(self)                

                QTimer.singleShot(10, self.center)
                
                self.thread_tg_1 = Thread_tg(
                    img_tg_check="images/Line_1/tg/",
                    bot_num="6724363071:AAHgCI3CtHgpi5GF8NAyw7vR0gRLF6FMoaY",
                    chat_id="-1002008064425",
                )
                self.thread_tg_2 = Thread_tg(
                    img_tg_check="images/Line_2/tg/",
                    bot_num="6446699116:AAGJEdSDleg3HYsIXKoDXKNyftnwzgmPduk",
                    chat_id="-1002100830067",
                )
                # self.thread_tg_3 = Thread_tg(
                #     img_tg_check="images/Line_3/tg/",
                #     bot_num="6446699116:AAGJEdSDleg3HYsIXKoDXKNyftnwzgmPduk",
                #     chat_id="-1002100830067",
                # )

                basedir_1 = os.path.dirname("models_1" + "/")
                model_list_1 = os.listdir(basedir_1)

                basedir_2 = os.path.dirname("models_2" + "/")
                model_list_2 = os.listdir(basedir_2)

                # basedir_3 = os.path.dirname("models_3" + "/")
                # model_list_3 = os.listdir(basedir_3)

                self.model_box.addItems(model_list_1)
                self.model_box.currentTextChanged.connect(self.model_change)

                self.model_box_2.addItems(model_list_2)
                self.model_box_2.currentTextChanged.connect(self.model_change)

                # self.model_box_3.addItems(model_list_3)
                # self.model_box_3.currentTextChanged.connect(self.model_change)

                self.thread_1 = Thread(
                    camera_path="images/Line_1/camera/",
                    check_path="images/Line_1/source/",
                    file_path="images/Line_1/source/",
                    result_path_ok="images/Line_1/ok/",
                    result_path_defect="images/Line_1/defect/",
                    model_path="models_1",
                    path_for_tg="images/Line_1/tg",
                )

                self.thread_test_1 = Thread(
                    camera_path="images/Line_1/camera/",
                    check_path="images/Line_1/source/",
                    file_path="images/Line_1/source/",
                    result_path_ok="images/Line_1/ok/",
                    result_path_defect="images/Line_1/defect/",
                    model_path="models_1",
                    path_for_tg="images/Line_1/defect/",
                )

                self.thread_2 = Thread(
                    camera_path="images/Line_2/camera/",
                    check_path="images/Line_2/source/",
                    file_path="images/Line_2/source/",
                    result_path_ok="images/Line_2/ok/",
                    result_path_defect="images/Line_2/defect/",
                    model_path="models_2",
                    path_for_tg="images/Line_2/tg",
                )

                self.thread_test_2 = Thread(
                    camera_path="images/Line_2/camera/",
                    check_path="images/Line_2/source/",
                    file_path="images/Line_2/source/",
                    result_path_ok="images/Line_2/ok/",
                    result_path_defect="images/Line_2/defect/",
                    model_path="models_2",
                    path_for_tg="images/Line_2/defect/",
                )

                # self.thread_3 = Thread(
                #     camera_path="images/Line_3/camera/",
                #     check_path="images/Line_3/source/",
                #     file_path="images/Line_3/source/",
                #     result_path_ok="images/Line_3/ok/",
                #     result_path_defect="images/Line_3/defect/",
                #     model_path="models_3",
                #     path_for_tg="images/Line_3/tg",
                # )

                # self.thread_test_3 = Thread(
                #     camera_path="images/Line_3/camera/",
                #     check_path="images/Line_3/source/",
                #     file_path="images/Line_3/source/",
                #     result_path_ok="images/Line_3/ok/",
                #     result_path_defect="images/Line_3/defect/",
                #     model_path="models_3",
                #     path_for_tg="images/Line_3/defect/",
                # )

                """ 1-я ЛИНИЯ """
                self.button_stop.pressed.connect(
                    lambda: self.button_stop_func(
                        thread_num=self.thread_1,
                        thread_tg=self.thread_tg_1,
                        thread_test_num=self.thread_test_1,
                        button_work=self.button_work,
                        button_test=self.button_test,
                        defect=self.defect,
                        main_pic=self.main_pic,
                    )
                )

                self.button_work.pressed.connect(
                    lambda: self.button_work_func(
                        model_box=self.model_box,
                        thread_num=self.thread_1,
                        thread_tg=self.thread_tg_1,
                        button_work=self.button_work,
                        button_test=self.button_test,
                        defect=self.defect,
                        main_pic=self.main_pic,
                    )
                )

                self.thread_1.result_no_data.connect(
                    lambda result_no_data: self.stop_thread(
                        result_no_data, thread_num=self.thread_1
                    )
                )

                self.button_test.pressed.connect(
                    lambda: self.button_test_func(
                        model_box=self.model_box,
                        thread_test_num=self.thread_test_1,
                        button_work=self.button_work,
                        button_test=self.button_test,
                        defect=self.defect,
                        main_pic=self.main_pic,
                    )
                )

                self.button_send_comm.pressed.connect(
                    lambda: self.button_text_send_func(
                        text_send_box=self.text_send,
                        bot_num="6724363071:AAHgCI3CtHgpi5GF8NAyw7vR0gRLF6FMoaY",
                        chat_id="-1002008064425",
                    )
                )

                """ 2-я ЛИНИЯ """
                self.button_stop_2.pressed.connect(
                    lambda: self.button_stop_func(
                        thread_num=self.thread_2,
                        thread_tg=self.thread_tg_2,
                        thread_test_num=self.thread_test_2,
                        button_work=self.button_work_2,
                        button_test=self.button_test_2,
                        defect=self.defect_2,
                        main_pic=self.main_pic_2,
                    )
                )

                self.button_work_2.pressed.connect(
                    lambda: self.button_work_func(
                        model_box=self.model_box_2,
                        thread_num=self.thread_2,
                        thread_tg=self.thread_tg_2,
                        button_work=self.button_work_2,
                        button_test=self.button_test_2,
                        defect=self.defect_2,
                        main_pic=self.main_pic_2,
                    )
                )

                self.thread_2.result_no_data.connect(
                    lambda result_no_data: self.stop_thread(
                        result_no_data, thread_num=self.thread_2
                    )
                )

                self.button_test_2.pressed.connect(
                    lambda: self.button_test_func(
                        model_box=self.model_box_2,
                        thread_test_num=self.thread_test_2,
                        button_work=self.button_work_2,
                        button_test=self.button_test_2,
                        defect=self.defect_2,
                        main_pic=self.main_pic_2,
                    )
                )

                self.button_send_comm_2.pressed.connect(
                    lambda: self.button_text_send_func(
                        text_send_box=self.text_send_2,
                        bot_num="6446699116:AAGJEdSDleg3HYsIXKoDXKNyftnwzgmPduk",
                        chat_id="-1002100830067",
                    )
                )

                # """ 3-я ЛИНИЯ """
                # self.button_stop_3.pressed.connect(
                #     lambda: self.button_stop_func(
                #         thread_num=self.thread_3,
                #         thread_tg=self.thread_tg_3,
                #         thread_test_num=self.thread_test_3,
                #         button_work=self.button_work_3,
                #         button_test=self.button_test_3,
                #         defect=self.defect_3,
                #         main_pic=self.main_pic_3,
                #     )
                # )

                # self.button_work_3.pressed.connect(
                #     lambda: self.button_work_func(
                #         model_box=self.model_box_3,
                #         thread_num=self.thread_3,
                #         thread_tg=self.thread_tg_3,
                #         button_work=self.button_work_3,
                #         button_test=self.button_test_3,
                #         defect=self.defect_3,
                #         main_pic=self.main_pic_3,
                #     )
                # )

                # self.thread_3.result_no_data.connect(
                #     lambda result_no_data: self.stop_thread(
                #         result_no_data, thread_num=self.thread_3
                #     )
                # )

                # self.button_test_3.pressed.connect(
                #     lambda: self.button_test_func(
                #         model_box=self.model_box_3,
                #         thread_test_num=self.thread_test_3,
                #         button_work=self.button_work_3,
                #         button_test=self.button_test_3,
                #         defect=self.defect_3,
                #         main_pic=self.main_pic_3,
                #     )
                # )

                # ''' Добавить 3-го бота на ТГ '''

                # self.button_send_comm_3.pressed.connect(
                #     lambda: self.button_text_send_func(
                #         text_send_box=self.text_send_3,
                #         bot_num="6446699116:AAGJEdSDleg3HYsIXKoDXKNyftnwzgmPduk",
                #         chat_id="-1002100830067",
                #     )
                # )

            def model_change(self, path_dir):
                ''' Вывод имени текущей модели '''
                pass

            def stop_thread(self, check, thread_num):
                ''' Остановить Thread '''

                thread_num.stop()

            def button_text_send_func(self, text_send_box, bot_num, chat_id):
                ''' Отправка сообщений в ТГ через форму пользователя '''
                message_box = text_send_box.toPlainText()
                if message_box:
                    bot = telepot.Bot(bot_num)
                    try:
                        bot.sendMessage(chat_id, message_box)
                        text_send_box.clear()
                    except FileNotFoundError:
                        pass

            def button_stop_func(
                self,
                thread_num,
                thread_tg,
                thread_test_num,
                button_work,
                button_test,
                defect,
                main_pic,
            ):
                ''' Функция остановки работы модели (как теста, так и рабочей):
                сброс стилей всех кнопок и полей, релиз всех кнопок,
                очистка поля с изображением, остановка Thread для отправки изображений в ТГ '''

                thread_tg.stop()
                button_work.setEnabled(True)
                thread_num.stop()
                thread_test_num.stop()
                button_work.setStyleSheet(normal_button_state)
                button_test.setEnabled(True)
                button_test.setStyleSheet(normal_button_state)
                defect.setStyleSheet(bg_signal_no_data)
                main_pic.clear()
                defect.setText("СИГНАЛ")

            def button_work_func(
                self,
                model_box,
                thread_num,
                thread_tg,
                button_work,
                button_test,
                defect,
                main_pic,
            ):
                ''' Запуск основной работы модели(QThread), запуск Thread для отправки сообщений в ТГ,
                установка стиля конпки Режим Работа в Зеленый, заморозка кнопки Тестовый режим,
                отправка изображения в поле для изображения, если сигнал брак '''

                thread_tg.start()
                thread_tg.send_current_model_box(model_box.currentText())
                thread_num.start()
                button_work.setStyleSheet(green_button_state)
                button_test.setDisabled(True)
                button_test.setStyleSheet(normal_button_state)
                thread_num.send_current_model_box(model_box.currentText())
                thread_num.result_norm.connect(
                    lambda result_norm: self.show_pic(result_norm, main_pic)
                )
                thread_num.result_defect.connect(
                    lambda result_defect: self.show_pic(result_defect, main_pic)
                )

                thread_num.text.connect(defect.setText)
                thread_num.text.connect(
                    lambda text: self.change_bg_signal(text, defect, main_pic)
                )
                thread_num.result_no_data.connect(defect.setText)
                thread_num.result_no_data.connect(
                    lambda result_no_data: self.change_bg_signal_no_data(
                        result_no_data,
                        main_pic,
                        defect,
                    )
                )

            def button_test_func(
                self,
                model_box,
                thread_test_num,
                button_work,
                button_test,
                defect,
                main_pic,
            ):
                ''' Запуск тестовой работы модели(QThread),
                установка стиля конпки Тестовый Режим в Зеленый и кнопки Режим Работа в норм,
                заморозка кнопки Режим Работа, отправка изображения в поле для изображения, если сигнал брак, 
                смена стиля поля Сигнал при отсутствии входящих данных  '''

                button_work.setDisabled(True)
                thread_test_num.start()
                button_work.setStyleSheet(normal_button_state)
                button_test.setStyleSheet(green_button_state)
                thread_test_num.send_current_model_box(model_box.currentText())
                thread_test_num.result_norm.connect(
                    lambda result_norm: self.show_pic(result_norm, main_pic)
                )
                
                thread_test_num.result_defect.connect(
                    lambda result_defect: self.show_pic(result_defect, main_pic)
                )
                thread_test_num.text.connect(defect.setText)
                thread_test_num.text.connect(
                    lambda text: self.change_bg_signal(text, defect, main_pic)
                )
                
                thread_test_num.result_no_data.connect(defect.setText)
                thread_test_num.result_no_data.connect(
                    lambda result_no_data: self.change_bg_signal_no_data(
                        result_no_data, main_pic, defect
                    )
                )

            def change_bg_signal(self, check, defect, main_pic):
                ''' Смена стиля поля Сигнал '''

                if check == "НОРМА":
                    defect.setStyleSheet(bg_signal_norm)
                    # main_pic.clear()
                elif check == "БРАК":
                    defect.setStyleSheet(bg_sinal_defect)

            def change_bg_signal_no_data(self, check, main_pic, defect):
                '''При отсутствии входящих ихображений меняет стиль рамки сигнала'''
                main_pic.clear()
                defect.setStyleSheet(bg_signal_no_data)

            def show_pic(self, str_root: str, main_pic: str) -> None:
                '''Показывает изображение в рамке'''                                
                main_pic.setPixmap(QPixmap(str_root))

            def center(self):
                qr=self.frameGeometry()           
                cp=self.screen().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())


        app = QApplication(sys.argv)

        app.setWindowIcon(QIcon("logo.svg"))
        app.setStyle("Fusion")
        w = MyWindow()
        w.show()
        app.exec()

except pidfile.AlreadyRunningError:
    pass
