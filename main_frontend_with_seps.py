import os
import sys
from PIL import Image
import shutil
import telepot
import pidfile
from itertools import product
from datetime import datetime


from PySide6.QtCore import QThread, Signal, Slot, QTimer, QTime
from PySide6.QtGui import QPixmap, QIcon, QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QLCDNumber, QLabel
from MainWindow import Ui_MainWindow
from style_sheet import (
    normal_button_state,
    green_button_state,
    bg_signal_norm,
    bg_signal_defect,
    bg_signal_no_data,
)
import time
import locale
locale.setlocale(locale.LC_ALL, 'ru')

from classes import Thread_tg, Thread

def main():

    try:
        from ctypes import windll  # Only exists on Windows.
        myappid = "QC-Monitoring"
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass


    try:
        with pidfile.PIDFile("example.pid"):
            class MyWindow(QMainWindow, Ui_MainWindow):
                def __init__(self, *args, obj=None, **kwargs):
                    super(MyWindow, self).__init__(*args, **kwargs)
                    self.setupUi(self)                

                    QTimer.singleShot(10, self.center)

                    basedir_1 = os.path.dirname("models_1" + "/")
                    model_list_1 = os.listdir(basedir_1)
                
                    # basedir_3 = os.path.dirname("models_3" + "/")
                    # model_list_3 = os.listdir(basedir_3)
                    TOKEN = None
                    
                    with open("token.txt") as f:
                        TOKEN = f.read().strip()

                    self.model_box.addItems(model_list_1)
                    self.model_box.currentTextChanged.connect(self.model_change)

                    self.thread_tg_1 = Thread_tg(
                        img_tg_check="images/Line_1/tg/",
                        bot_num=TOKEN,
                        chat_id="-1002008064425",
                    )

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
                            text_send="Конец работы!",
                            bot_num=TOKEN,
                            chat_id="-1002008064425",
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
                            text_send="Начало работы!",
                            bot_num=TOKEN,
                            chat_id="-1002008064425",
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

                
                def update_lcd(self):
                    ''' Функция обновления LCD '''                
                    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())                
                    self.label_time.setText(formatted_time)           

                def the_button_was_pressed(self, checked):
                    self.button_is_checked = checked
                    print(self.button_is_checked)

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
                    text_send,
                    bot_num,
                    chat_id,
                ):
                    ''' Функция остановки работы модели (как теста, так и рабочей):
                    сброс стилей всех кнопок и полей, релиз всех кнопок,
                    очистка поля с изображением, остановка Thread для отправки изображений в ТГ '''

                    if str(button_work.styleSheet()) == green_button_state:
                        time_tg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        text = text_send + ' ' + time_tg
                        bot = telepot.Bot(bot_num)
                        bot.sendMessage(chat_id, text)
                    else:
                        pass
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
                    text_send,
                    bot_num,
                    chat_id,
                ):
                    ''' Запуск основной работы модели(QThread), запуск Thread для отправки сообщений в ТГ,
                    установка стиля конпки Режим Работа в Зеленый, заморозка кнопки Тестовый режим,
                    отправка изображения в поле для изображения, если сигнал брак ''' 
                    if str(button_work.styleSheet()) != green_button_state:
                        time_tg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        text = text_send + ' ' + time_tg
                        bot = telepot.Bot(bot_num)
                        bot.sendMessage(chat_id, text)
                    else:
                        pass

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
                        defect.setStyleSheet(bg_signal_defect)                    

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

if __name__ == "__main__":
    main()