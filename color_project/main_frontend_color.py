import os
import sys
import shutil
from time import sleep
from PIL import Image
import shutil
import telepot
import requests
import pidfile
import time
import locale
locale.setlocale(locale.LC_ALL, 'ru')

from PySide6.QtCore import QThread, Signal, Slot, QTimer
from PySide6.QtGui import QPixmap, QIcon, QGuiApplication, QIntValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar
from MainWindow_color import Ui_MainWindow

from csv import DictWriter
from lab_space_calculation import *
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976, delta_e_cie1994, delta_e_cie2000
def main():
            
    try:
        from ctypes import windll  # Only exists on Windows.
        myappid = "QC-Color"
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass


    try:
        with pidfile.PIDFile("example.pid"):
            "Starting program execution"

            # class Thread_tg(QThread):
            #     ''' Класс отправки сообщений в Телеграмм '''

            #     def __init__(
            #         self,
            #         img_tg_check: str,
            #         bot_num: str,
            #         chat_id: str,
            #     ) -> None:
            #         super().__init__()
            #         self.img_tg_check = img_tg_check
            #         self.bot_num = bot_num
            #         self.chat_id = chat_id

            #     @Slot()
            #     def run(self):
            #         '''Реализация отправки сообщения в ТГ'''

            #         self.data = self.send_current_model_box(self.data)
            #         self.tg_is_running = True
            #         while self.tg_is_running:
            #             try:
            #                 self.check_tg = os.listdir(self.img_tg_check)
            #                 if self.check_tg:
            #                     self.send_tg = self.send_telegram(
            #                         self.data,
            #                         bot_num=self.bot_num,
            #                         chat_id=self.chat_id,
            #                         photo_path=(
            #                             self.img_tg_check + os.listdir(self.img_tg_check)[0]
            #                         ),
            #                     )
            #                     os.remove(
            #                         (self.img_tg_check + os.listdir(self.img_tg_check)[0])
            #                     )

            #             except FileNotFoundError:
            #                 pass

            #     def send_telegram(self, 
            #         data: str, 
            #         bot_num: str, 
            #         chat_id: str, 
            #         photo_path: str) -> None:
            #         '''Функция отправки сообщения в ТГ'''

            #         bot_url = "https://api.telegram.org/bot" + bot_num + "/sendPhoto"
            #         payload = {"chat_id": chat_id, "caption": data}

            #         with open(photo_path, "rb") as image_file:
            #             send_photo_tg = requests.post(
            #                 url=bot_url,
            #                 data=payload,
            #                 files={"photo": image_file},
            #             )

            #     def stop(self) -> None:
            #         ''' Остановить Thread'''

            #         self.tg_is_running = False

            #     def send_current_model_box(self, data: str) -> str:
            #         '''Получение имени текущей модели извне'''

            #         self.data = data
            #         return self.data

            class Thread(QThread):
                '''Класс Thread для основного действия: смена цвета CMYK-RGB и инференс модели предсказания'''

                current_delta = Signal(str)
                lab_current_value = Signal(str)
                result_no_data = Signal(str)

                def __init__(
                    self,
                    img_src: str,                    
                    set_lab: str,
                ) -> None:
                    super().__init__()
                    self.img_src = img_src                    
                    self.set_lab = set_lab

                @Slot()
                def run(self):
                    
                    '''Запуск методов класса'''
                    self.is_running = True
                    
                    while self.is_running:
                        self.quantity = self.get_quantity(self.quantity)
                        self.ctrl_delta = self.get_delta_e_set(self.ctrl_delta)
                        try:
                            self.img_check = os.listdir(self.img_src)                            
                            if len(self.img_check) >= int(self.quantity):

                                basedir_move = os.path.dirname('dataset_diff_color' + "/")
                                basedir_src = basedir_move + '/current_resized/'
                                basedir_trg = basedir_move + '/current_resized_2/'

                                count_for_make_list = sorted(os.listdir(basedir_src), key=lambda x: int(x.rsplit('_', 1)[1].rsplit('.', 1)[0]))[::-1][0]
                                count_result = int(count_for_make_list.rsplit('_', 1)[1].rsplit('.', 1)[0])
                                
                                img_check_sorted = make_list(basedir_trg, basedir_src, count_result)

                                self.lab_current, self.current_lab_space, _ = calculate_lab_space(                                                    
                                                    img_src=self.img_src,
                                                    image_list=self.img_check,
                                                    quantity=int(self.quantity),
                                )
                                set_lab_space = [float(n) for n in self.set_lab.text().replace(" : ", " ").split(" ")]
                                color_fact = LabColor(lab_l=set_lab_space[0], lab_a=set_lab_space[1], lab_b=set_lab_space[2])

                                color_current = LabColor(lab_l=self.current_lab_space[0], lab_a=self.current_lab_space[1], lab_b=self.current_lab_space[2])
                                self.delta_e_1994 = delta_e_cie1994(color_fact, color_current)

                                self.current_delta.emit(str(self.delta_e_1994.round(2)))
                                self.lab_current_value.emit(self.lab_current)

                                shutil.move(os.path.join(basedir_src, img_check_sorted[-1]), basedir_trg)
                                # img_cut_sorted = img_check_sorted[-10:]
                                # for files in img_cut_sorted:
                                #     shutil.move(os.path.join(basedir_src, files), basedir_trg)

                                # The list of column names as mentioned in the CSV file
                                headersCSV = ["Дата", "Время", "L контр.", "a контр.", "b контр.",\
                                "L", "a", "b", "DeltaE контр.", "DeltaE факт."] # , "Дата/время", "Марка материала"                                

                                current_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())

                                dict = {"Дата": current_time.rsplit(' ', 1)[0], "Время": current_time.rsplit(' ', 1)[1],\
                                        "L контр.": set_lab_space[0], "a контр.": set_lab_space[1], "b контр.": set_lab_space[2],\
                                        "L": self.current_lab_space[0], "a": self.current_lab_space[1], "b": self.current_lab_space[2],\
                                        "DeltaE контр.": self.ctrl_delta, "DeltaE факт.": self.delta_e_1994.round(2)} # , "Марка материала"

                                with open("database.csv", "a", newline="") as f_object:
                                    dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
                                    dictwriter_object.writerow(dict)
                                    f_object.close()

                                sleep(0.1)
                            else:
                                self.result_no_data.emit("Ожидание данных!")
                        except (TypeError, IndexError):
                            pass

                def get_delta_e_set(self, ctrl_delta: str):
                    '''Получение количества изображений извне'''

                    self.ctrl_delta = ctrl_delta                    
                    return self.ctrl_delta

                def get_quantity(self, quantity: str):
                    '''Получение количества изображений извне'''

                    self.quantity = quantity                    
                    return self.quantity

                def stop(self):
                    ''' Остановить Thread'''

                    self.is_running = False
                

            class MyWindow(QMainWindow, Ui_MainWindow):
                def __init__(self, *args, obj=None, **kwargs):
                    super(MyWindow, self).__init__(*args, **kwargs)
                    self.setupUi(self)                

                    QTimer.singleShot(10, self.center)

                    '''Create timer to update the LCD'''
                    self.timer = QTimer()
                    self.timer.timeout.connect(self.update_lcd)
                    self.timer.start(1000)
                    self.update_lcd()                    

                    self.lineEdit.setValidator(QIntValidator(100, 300, self))
                    self.lineEdit.setPlaceholderText('>150')

                    self.lineEdit_2.setValidator(QIntValidator(1, 10, self))
                    self.lineEdit_2.setPlaceholderText('1-10')

                    self.set_ctrl_delta.pressed.connect(
                        lambda: self.set_delta_e(
                            ctrl_delta=self.ctrl_delta,
                            set_delta=self.lineEdit_2,
                        )
                    )
                    self.set_img_quantity.pressed.connect(
                        lambda: self.set_img_quant(
                            label_quantity=self.label_quantity,
                            set_quantity=self.lineEdit,
                        )
                    )

                    
                    basedir_1 = os.path.dirname('dataset_diff_color' + '/')
                    image_list_1 = os.listdir(basedir_1 + '/' + '3_cropped_resized/')
                    image_list_2 = os.listdir(basedir_1 + '/' + 'current_resized/')

                    self.thread_1 = Thread(
                        img_src=basedir_1 + '/' + 'current_resized' + '/',
                        set_lab=self.set_lab,                        
                    )

                    self.set_lab_ctrl_value.pressed.connect(
                        lambda: self.set_lab_control(
                            basedir_1=basedir_1,
                            image_list_1=image_list_1,
                            quantity=int(self.label_quantity.text()),
                            set_lab=self.set_lab,
                            defect=self.defect,
                        )
                    )
                    
                    self.button_stop.pressed.connect(
                        lambda: self.button_stop_func(
                            thread_num=self.thread_1,
                            button_work=self.button_work,
                            defect=self.defect,
                        ))

                    self.button_work.pressed.connect(
                        lambda: self.set_work(
                            thread_num=self.thread_1,
                            basedir_1=basedir_1,
                            image_list_2=image_list_2,
                            label_quantity=self.label_quantity,
                            button_work=self.button_work,
                            set_lab=self.set_lab,
                            current_lab=self.current_lab,                            
                            ctrl_delta=self.ctrl_delta,
                            current_delta_show=self.current_delta_show,
                            defect=self.defect,
                        )
                    )
                    # self.button_stop.pressed.connect(
                    #     lambda: self.stop_work(
                    #         delta_fact=self.delta_fact, 
                    #         ctrl_delta=self.ctrl_delta, 
                    #         defect=self.defect,
                    #     )
                    # )

                def set_work(self, thread_num, label_quantity,
                                    button_work, basedir_1, 
                                    image_list_2, set_lab, 
                                    current_lab, ctrl_delta,
                                    current_delta_show, defect):
                    thread_num.start()
                    thread_num.get_quantity(label_quantity.text())
                    thread_num.get_delta_e_set(ctrl_delta.text())
                    button_work.setStyleSheet(green_button_state)
                    button_work.setDisabled(True)
                    thread_num.lab_current_value.connect(
                        lambda lab_current_value: self.set_lab_current(lab_current_value, current_lab)
                    )
                    thread_num.current_delta.connect(lambda current_delta: self.calc_delta_e(
                        current_delta, ctrl_delta, current_delta_show, defect))

                def set_no_data(self, result_no_data, defect):
                    if result_no_data is None:
                        pass
                    else:
                        defect.setText(result_no_data)
                        defect.setStyleSheet(bg_signal_no_data)

                def button_stop_func(
                    self,
                    thread_num,
                    button_work,
                    defect,
                    # bot_num,
                    # chat_id,
                ):
                    ''' Функция остановки работы модели:
                    сброс стилей всех кнопок и полей, релиз всех кнопок,
                    остановка Thread '''

                    # if str(button_work.styleSheet()) == green_button_state:
                    #     bot = telepot.Bot(bot_num)
                    #     bot.sendMessage(chat_id, text_send)
                    # else:
                    #     pass
                    defect.setText("СИГНАЛ")                    
                    defect.setStyleSheet(bg_signal_no_data)
                    thread_num.stop()
                    button_work.setEnabled(True)
                    button_work.setStyleSheet(normal_button_state)

                # def stop_thread(self, check, thread_num):
                #     ''' Остановить Thread для остановки когда нет изображений в папке'''
                #     thread_num.stop()

                def calc_delta_e(self, current_delta, ctrl_delta, current_delta_show, defect):
                    current_delta_show.setText(current_delta)

                    if float(current_delta) < float(ctrl_delta.text()):
                        defect.setText('Норма') 
                        defect.setStyleSheet(bg_signal_norm)
                    elif float(current_delta) >= float(ctrl_delta.text()):
                        defect.setText('Ошибка')
                        defect.setStyleSheet(bg_signal_defect)                        

                def set_lab_current(self, lab_current_value, current_lab):
                    current_lab.setText(lab_current_value)

                def set_lab_control(self, basedir_1, image_list_1, quantity, set_lab, defect):
                    try:                        
                        lab_control_value, _ , _ = calculate_lab_space(                                                    
                                                        basedir_1 + '/3_cropped_resized' + '/',
                                                        image_list_1,
                                                        quantity,
                        )
                        set_lab.setText(lab_control_value)
                    except IndexError:
                        defect.setText('Ожидание данных!')
                        defect.setStyleSheet(bg_signal_no_data)
                def change_bg_signal(self, current_delta, ctrl_delta, defect):
                    ''' Смена стиля поля Сигнал '''

                    if float(current_delta.text()) <= float(ctrl_delta.text()):
                        defect.setStyleSheet(bg_signal_norm)                        
                    elif float(current_delta.text()) > float(ctrl_delta.text()):
                        defect.setStyleSheet(bg_signal_defect)

                def set_img_quant(self, label_quantity, set_quantity) -> None:
                    label_quantity.setText(set_quantity.text())
                    set_quantity.clear()

                def set_delta_e(self, ctrl_delta, set_delta) -> None:                    
                    ctrl_delta.setText(set_delta.text())
                    set_delta.clear()

                def update_lcd(self):
                    ''' Функция обновления LCD '''                
                    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
                    self.label_time.setText(formatted_time)
                 

                # def change_bg_signal_no_data(self, check, main_pic, defect):
                #     '''При отсутствии входящих ихображений меняет стиль рамки сигнала'''
                #     main_pic.clear()
                #     defect.setStyleSheet(bg_signal_no_data)

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

main()