# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_color.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 729)
        MainWindow.setStyleSheet(u"background: #36353f;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QScrollBar:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #323140;\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"\n"
"QScrollBar::handle:vertical {\n"
"      background: #615e7d;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #323140;\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #323140;\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"      border: 2px solid grey;\n"
"      width: 3px;\n"
"      height: 3px;\n"
"      background: white;\n"
"  }\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"  }\n"
"\n"
"QLineEdit{\n"
"color: #efebef;\n"
"font: "
                        "10pt \"Verdana\";\n"
"background-color: #3c3b4b;\n"
"border-radius: 9px;\n"
"border: 1px solid #5f5f5f;\n"
"}\n"
"\n"
"QTextEdit{\n"
"color: #efebef;\n"
"font: 12pt \"Arial\";\n"
"background-color: #3c3b4b;\n"
"border-radius: 9px;\n"
"border: 1px solid #5f5f5f;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"border: 2px solid grey;\n"
"background: #3c3b4b;\n"
"width: 18px;\n"
"margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QComboBox{\n"
"color: #efebef;\n"
"background: #3c3b4b;\n"
"border-radius: 5px;\n"
"border: 1px solid #5f5f5f;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #28495c, stop: 1 #5c7d90);\n"
"color:#efebef;\n"
"border-radius: 12px;\n"
"border: 1px solid #636173;\n"
"outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3c3b4b, stop: 1 #4b4875);\n"
"border: 2px solid rgb(185, 185, 185);\n"
"color: rgb(221, 221, 221);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(x1: 0, "
                        "y1: 0, x2: 0, y2: 1, stop: 0 #5f5b98, stop: 1 #7f7ace);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 12px;\n"
"border: 1px solid rgb(189, 189, 189);\n"
"outline: 0px;\n"
"}\n"
"QLabel{\n"
"color:#efebef;\n"
"border: 0px solid #3c3b4b;\n"
"font: 10pt \"Verdana\";\n"
"}\n"
"\n"
"#set_lab{\n"
"color:#efebef;\n"
"border: 2px solid #3c3b4b;\n"
"font: 12pt \"Verdana\";\n"
"}\n"
"#current_lab{\n"
"color:#efebef;\n"
"border: 2px solid #3c3b4b;\n"
"font: 12pt \"Verdana\";\n"
"}\n"
"#current_delta_show{\n"
"color:#efebef;\n"
"border: 2px solid #3c3b4b;\n"
"font: 12pt \"Verdana\";\n"
"}\n"
"#delta_fact {\n"
"color:#efebef;\n"
"border: 2px solid #3c3b4b;\n"
"font: 12pt \"Verdana\";\n"
"}\n"
"\n"
"#label_quantity {\n"
"color:#efebef;\n"
"border: 2px solid #3c3b4b;\n"
"font: 12pt \"Verdana\";\n"
"}\n"
"\n"
"#ctrl_delta {\n"
"color:#efebef;\n"
"border: 2px solid #3c3b4b;\n"
"font: 12pt \"Verdana\";\n"
"}\n"
"\n"
"#line_number_1 {\n"
"color:#efebef;\n"
"border: 0px;\n"
"font: 22pt \"Verdana\";\n"
"}\n"
"\n"
"QDateTimeEdit{\n"
""
                        "border: 1px solid #3c3b4b;\n"
"color:#efebef;\n"
"}\n"
"#defect {\n"
"background-color: #6c6a89;\n"
"border: 1px;\n"
"border-radius: 15px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.line_number_1 = QLabel(self.centralwidget)
        self.line_number_1.setObjectName(u"line_number_1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_number_1.sizePolicy().hasHeightForWidth())
        self.line_number_1.setSizePolicy(sizePolicy)
        self.line_number_1.setMinimumSize(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(97, 97, 97, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(54, 53, 63, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(239, 235, 239, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(239, 235, 239, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.line_number_1.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.line_number_1.setFont(font)
        self.line_number_1.setMouseTracking(True)
        self.line_number_1.setAutoFillBackground(False)
        self.line_number_1.setFrameShape(QFrame.NoFrame)
        self.line_number_1.setFrameShadow(QFrame.Plain)
        self.line_number_1.setLineWidth(0)
        self.line_number_1.setMidLineWidth(0)
        self.line_number_1.setTextFormat(Qt.AutoText)
        self.line_number_1.setScaledContents(False)
        self.line_number_1.setAlignment(Qt.AlignCenter)
        self.line_number_1.setMargin(0)
        self.line_number_1.setIndent(-1)

        self.horizontalLayout_5.addWidget(self.line_number_1)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_5)

        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        sizePolicy.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy)
        self.label_time.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_time.setFont(font1)
        self.label_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_time.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_22.addWidget(self.label_time)


        self.verticalLayout.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_stop = QPushButton(self.centralwidget)
        self.button_stop.setObjectName(u"button_stop")
        self.button_stop.setMinimumSize(QSize(150, 50))
        self.button_stop.setMaximumSize(QSize(150, 50))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.button_stop.setFont(font2)
        self.button_stop.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.button_stop)

        self.button_work = QPushButton(self.centralwidget)
        self.button_work.setObjectName(u"button_work")
        sizePolicy.setHeightForWidth(self.button_work.sizePolicy().hasHeightForWidth())
        self.button_work.setSizePolicy(sizePolicy)
        self.button_work.setMinimumSize(QSize(150, 50))
        self.button_work.setMaximumSize(QSize(150, 50))
        self.button_work.setFont(font2)
        self.button_work.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.button_work)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, 10)
        self.defect = QLabel(self.centralwidget)
        self.defect.setObjectName(u"defect")
        sizePolicy.setHeightForWidth(self.defect.sizePolicy().hasHeightForWidth())
        self.defect.setSizePolicy(sizePolicy)
        self.defect.setMinimumSize(QSize(250, 35))
        self.defect.setFont(font1)
        self.defect.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.defect)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(40)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 20, -1, 20)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QSize(240, 30))

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setMaximumSize(QSize(100, 30))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        self.pushButton.setFont(font3)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(70, 30))
        self.lineEdit.setMaximumSize(QSize(70, 30))
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_quantity = QLabel(self.centralwidget)
        self.label_quantity.setObjectName(u"label_quantity")
        sizePolicy.setHeightForWidth(self.label_quantity.sizePolicy().hasHeightForWidth())
        self.label_quantity.setSizePolicy(sizePolicy)
        self.label_quantity.setMinimumSize(QSize(50, 30))
        self.label_quantity.setStyleSheet(u"")
        self.label_quantity.setAlignment(Qt.AlignCenter)
        self.label_quantity.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_quantity)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QSize(150, 30))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_5)

        self.set_img_quantity = QPushButton(self.centralwidget)
        self.set_img_quantity.setObjectName(u"set_img_quantity")
        sizePolicy.setHeightForWidth(self.set_img_quantity.sizePolicy().hasHeightForWidth())
        self.set_img_quantity.setSizePolicy(sizePolicy)
        self.set_img_quantity.setMinimumSize(QSize(100, 30))
        self.set_img_quantity.setMaximumSize(QSize(100, 30))
        self.set_img_quantity.setFont(font3)

        self.horizontalLayout.addWidget(self.set_img_quantity)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(70, 30))
        self.lineEdit_2.setMaximumSize(QSize(70, 30))
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.ctrl_delta = QLabel(self.centralwidget)
        self.ctrl_delta.setObjectName(u"ctrl_delta")
        sizePolicy.setHeightForWidth(self.ctrl_delta.sizePolicy().hasHeightForWidth())
        self.ctrl_delta.setSizePolicy(sizePolicy)
        self.ctrl_delta.setMinimumSize(QSize(50, 30))
        self.ctrl_delta.setStyleSheet(u"")
        self.ctrl_delta.setAlignment(Qt.AlignCenter)
        self.ctrl_delta.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.ctrl_delta)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(150, 30))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.set_ctrl_delta = QPushButton(self.centralwidget)
        self.set_ctrl_delta.setObjectName(u"set_ctrl_delta")
        sizePolicy.setHeightForWidth(self.set_ctrl_delta.sizePolicy().hasHeightForWidth())
        self.set_ctrl_delta.setSizePolicy(sizePolicy)
        self.set_ctrl_delta.setMinimumSize(QSize(100, 30))
        self.set_ctrl_delta.setMaximumSize(QSize(100, 30))
        self.set_ctrl_delta.setFont(font3)

        self.horizontalLayout_4.addWidget(self.set_ctrl_delta)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.set_lab_ctrl_value = QPushButton(self.centralwidget)
        self.set_lab_ctrl_value.setObjectName(u"set_lab_ctrl_value")
        sizePolicy.setHeightForWidth(self.set_lab_ctrl_value.sizePolicy().hasHeightForWidth())
        self.set_lab_ctrl_value.setSizePolicy(sizePolicy)
        self.set_lab_ctrl_value.setMinimumSize(QSize(200, 40))
        self.set_lab_ctrl_value.setMaximumSize(QSize(200, 40))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setBold(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.set_lab_ctrl_value.setFont(font4)
        self.set_lab_ctrl_value.setAcceptDrops(False)
        self.set_lab_ctrl_value.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_16.addWidget(self.set_lab_ctrl_value)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(200, 25))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.set_lab = QLabel(self.centralwidget)
        self.set_lab.setObjectName(u"set_lab")
        sizePolicy.setHeightForWidth(self.set_lab.sizePolicy().hasHeightForWidth())
        self.set_lab.setSizePolicy(sizePolicy)
        self.set_lab.setMinimumSize(QSize(200, 30))
        self.set_lab.setMaximumSize(QSize(200, 30))
        self.set_lab.setLayoutDirection(Qt.LeftToRight)
        self.set_lab.setStyleSheet(u"")
        self.set_lab.setAlignment(Qt.AlignCenter)
        self.set_lab.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.set_lab)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(200, 25))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.current_lab = QLabel(self.centralwidget)
        self.current_lab.setObjectName(u"current_lab")
        sizePolicy.setHeightForWidth(self.current_lab.sizePolicy().hasHeightForWidth())
        self.current_lab.setSizePolicy(sizePolicy)
        self.current_lab.setMinimumSize(QSize(200, 30))
        self.current_lab.setMaximumSize(QSize(200, 30))
        self.current_lab.setStyleSheet(u"")
        self.current_lab.setAlignment(Qt.AlignCenter)
        self.current_lab.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_6.addWidget(self.current_lab)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(200, 25))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)


        self.verticalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.current_delta_show = QLabel(self.centralwidget)
        self.current_delta_show.setObjectName(u"current_delta_show")
        sizePolicy.setHeightForWidth(self.current_delta_show.sizePolicy().hasHeightForWidth())
        self.current_delta_show.setSizePolicy(sizePolicy)
        self.current_delta_show.setMinimumSize(QSize(200, 30))
        self.current_delta_show.setMaximumSize(QSize(200, 30))
        self.current_delta_show.setStyleSheet(u"")
        self.current_delta_show.setLineWidth(1)
        self.current_delta_show.setAlignment(Qt.AlignCenter)
        self.current_delta_show.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_8.addWidget(self.current_delta_show)


        self.verticalLayout_2.addLayout(self.verticalLayout_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, 10)
        self.comment = QLabel(self.centralwidget)
        self.comment.setObjectName(u"comment")
        sizePolicy.setHeightForWidth(self.comment.sizePolicy().hasHeightForWidth())
        self.comment.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comment.setPalette(palette1)
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(True)
        self.comment.setFont(font5)
        self.comment.setStyleSheet(u"")
        self.comment.setFrameShape(QFrame.NoFrame)
        self.comment.setLineWidth(0)
        self.comment.setMidLineWidth(0)
        self.comment.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.comment)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.text_send = QTextEdit(self.centralwidget)
        self.text_send.setObjectName(u"text_send")
        sizePolicy.setHeightForWidth(self.text_send.sizePolicy().hasHeightForWidth())
        self.text_send.setSizePolicy(sizePolicy)
        self.text_send.setMinimumSize(QSize(350, 70))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush4 = QBrush(QColor(60, 59, 75, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.text_send.setPalette(palette2)
        self.text_send.setFrameShape(QFrame.Box)
        self.text_send.setFrameShadow(QFrame.Plain)
        self.text_send.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.horizontalLayout_10.addWidget(self.text_send)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 20, -1, -1)
        self.button_send_comm = QPushButton(self.centralwidget)
        self.button_send_comm.setObjectName(u"button_send_comm")
        self.button_send_comm.setMinimumSize(QSize(150, 50))
        self.button_send_comm.setMaximumSize(QSize(150, 50))
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.button_send_comm.setFont(font6)
        self.button_send_comm.setAutoFillBackground(False)

        self.horizontalLayout_11.addWidget(self.button_send_comm)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.line_number_1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u0446\u0432\u0435\u0442\u0430", None))
        self.label_time.setText("")
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u041e\u041f", None))
        self.button_work.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u041f\u0423\u0421\u041a", None))
        self.defect.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0418\u0413\u041d\u0410\u041b", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_quantity.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.set_img_quantity.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.ctrl_delta.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Delta E (0-6)", None))
        self.set_ctrl_delta.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.set_lab_ctrl_value.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c Lab \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u043e\u0435 Lab \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.set_lab.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 Lab \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.current_lab.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Delta E \u0442\u0435\u043a\u0443\u0449\u0435\u0435", None))
        self.current_delta_show.setText("")
        self.comment.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u041c\u041c\u0415\u041d\u0422\u0410\u0420\u0418\u0419", None))
        self.button_send_comm.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0422\u041f\u0420\u0410\u0412\u0418\u0422\u042c", None))
    # retranslateUi

