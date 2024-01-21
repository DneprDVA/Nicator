# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(520, 990)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"background: #36353f;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(500, 0))
        palette = QPalette()
        brush = QBrush(QColor(54, 53, 63, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget::tab-bar {\n"
"alignment: center;\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that\n"
"it reads QTabBar _not_ QTabWidget */\n"
"\n"
"QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #524f70, stop: 0.4 #403e58,\n"
"stop: 0.5 #2f2d40, stop: 1.0 #24232d);\n"
"color:#efebef;\n"
"border: 2px solid #757575;\n"
"border-bottom-color: #757575; /* same as the pane color */\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"min-width: 8ex;\n"
"padding: 10px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"color:#efebef;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #28495c, stop: 0.4 #396984,\n"
"stop: 0.5 #396984, stop: 1.0 #4c8eb6);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #323140;\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"  QScrollBar::handle:vertical {\n"
"      background: #615e7d;\n"
"      min-height: 20px;\n"
"  }\n"
""
                        "  QScrollBar::add-line:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #323140;\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"  QScrollBar::sub-line:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #323140;\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"  QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"      border: 2px solid grey;\n"
"      width: 3px;\n"
"      height: 3px;\n"
"      background: white;\n"
"  }\n"
"\n"
"  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"  }\n"
"\n"
"QTextEdit{\n"
"color: #efebef;\n"
"font: 75 12pt \"Arial\";\n"
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
"QCom"
                        "boBox{\n"
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
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #5f5b98, stop: 1 #7f7ace);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 12px;\n"
"border: 1px solid rgb(189, 189, 189);\n"
"outline: 0px;\n"
"}\n"
"QLabel{\n"
"border: 1px solid #3c3b4b;\n"
"color:#efebef;\n"
"}\n"
"#defect {\n"
"background-color: #6c6a89;\n"
"border: 1px;\n"
"border-radius: 15px;\n"
"}\n"
"#main_pic {\n"
"background-color: #3c3b4b;\n"
"border: 1px solid #5f5f5f;\n"
""
                        "}\n"
"#defect_2 {\n"
"background-color: #6c6a89;\n"
"border: 1px;\n"
"border-radius: 15px;\n"
"}\n"
"#main_pic_2 {\n"
"background-color: #3c3b4b;\n"
"border: 1px solid #5f5f5f;\n"
"}\n"
"\n"
"")
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        sizePolicy.setHeightForWidth(self.tab_1.sizePolicy().hasHeightForWidth())
        self.tab_1.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setKerning(True)
        self.tab_1.setFont(font1)
        self.tab_1.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_number_1 = QLabel(self.tab_1)
        self.line_number_1.setObjectName(u"line_number_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_number_1.sizePolicy().hasHeightForWidth())
        self.line_number_1.setSizePolicy(sizePolicy2)
        palette1 = QPalette()
        brush1 = QBrush(QColor(97, 97, 97, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        brush2 = QBrush(QColor(239, 235, 239, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        brush3 = QBrush(QColor(239, 235, 239, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.line_number_1.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(False)
        self.line_number_1.setFont(font2)
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

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line_5 = QFrame(self.tab_1)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.model_box = QComboBox(self.tab_1)
        self.model_box.setObjectName(u"model_box")
        sizePolicy2.setHeightForWidth(self.model_box.sizePolicy().hasHeightForWidth())
        self.model_box.setSizePolicy(sizePolicy2)
        self.model_box.setMinimumSize(QSize(350, 25))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush4 = QBrush(QColor(60, 59, 75, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        brush5 = QBrush(QColor(0, 170, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush6 = QBrush(QColor(100, 100, 100, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush7 = QBrush(QColor(225, 225, 225, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush7)
        brush8 = QBrush(QColor(88, 88, 88, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        brush9 = QBrush(QColor(130, 130, 130, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        brush10 = QBrush(QColor(84, 84, 84, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.model_box.setPalette(palette2)
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setKerning(True)
        self.model_box.setFont(font3)
        self.model_box.setLayoutDirection(Qt.LeftToRight)
        self.model_box.setEditable(True)
        self.model_box.setCurrentText(u"")
        self.model_box.setMaxVisibleItems(20)
        self.model_box.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.model_box.setPlaceholderText(u"")

        self.horizontalLayout_4.addWidget(self.model_box)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.button_stop = QPushButton(self.tab_1)
        self.button_stop.setObjectName(u"button_stop")
        self.button_stop.setMinimumSize(QSize(150, 50))
        self.button_stop.setMaximumSize(QSize(150, 50))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.button_stop.setFont(font4)
        self.button_stop.setAutoFillBackground(False)

        self.horizontalLayout_3.addWidget(self.button_stop)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_test = QPushButton(self.tab_1)
        self.button_test.setObjectName(u"button_test")
        sizePolicy2.setHeightForWidth(self.button_test.sizePolicy().hasHeightForWidth())
        self.button_test.setSizePolicy(sizePolicy2)
        self.button_test.setMinimumSize(QSize(150, 50))
        self.button_test.setMaximumSize(QSize(150, 50))
        self.button_test.setFont(font4)
        self.button_test.setAutoFillBackground(False)
        self.button_test.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.button_test)

        self.button_work = QPushButton(self.tab_1)
        self.button_work.setObjectName(u"button_work")
        sizePolicy2.setHeightForWidth(self.button_work.sizePolicy().hasHeightForWidth())
        self.button_work.setSizePolicy(sizePolicy2)
        self.button_work.setMinimumSize(QSize(150, 50))
        self.button_work.setMaximumSize(QSize(150, 50))
        self.button_work.setFont(font4)
        self.button_work.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.button_work)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.defect = QLabel(self.tab_1)
        self.defect.setObjectName(u"defect")
        sizePolicy2.setHeightForWidth(self.defect.sizePolicy().hasHeightForWidth())
        self.defect.setSizePolicy(sizePolicy2)
        self.defect.setMinimumSize(QSize(140, 35))
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.defect.setFont(font5)
        self.defect.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.defect)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.main_pic = QLabel(self.tab_1)
        self.main_pic.setObjectName(u"main_pic")
        sizePolicy2.setHeightForWidth(self.main_pic.sizePolicy().hasHeightForWidth())
        self.main_pic.setSizePolicy(sizePolicy2)
        self.main_pic.setMinimumSize(QSize(300, 300))
        self.main_pic.setMaximumSize(QSize(350, 350))
        self.main_pic.setFrameShape(QFrame.Box)
        self.main_pic.setLineWidth(1)
        self.main_pic.setScaledContents(True)
        self.main_pic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.main_pic)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.comment = QLabel(self.tab_1)
        self.comment.setObjectName(u"comment")
        sizePolicy2.setHeightForWidth(self.comment.sizePolicy().hasHeightForWidth())
        self.comment.setSizePolicy(sizePolicy2)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comment.setPalette(palette3)
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(10)
        font6.setUnderline(True)
        self.comment.setFont(font6)
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
        self.text_send = QTextEdit(self.tab_1)
        self.text_send.setObjectName(u"text_send")
        sizePolicy2.setHeightForWidth(self.text_send.sizePolicy().hasHeightForWidth())
        self.text_send.setSizePolicy(sizePolicy2)
        self.text_send.setMinimumSize(QSize(350, 70))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.text_send.setPalette(palette4)
        self.text_send.setFrameShape(QFrame.Box)
        self.text_send.setFrameShadow(QFrame.Plain)
        self.text_send.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.horizontalLayout_10.addWidget(self.text_send)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.button_send_comm = QPushButton(self.tab_1)
        self.button_send_comm.setObjectName(u"button_send_comm")
        self.button_send_comm.setMinimumSize(QSize(150, 50))
        self.button_send_comm.setMaximumSize(QSize(150, 50))
        font7 = QFont()
        font7.setFamilies([u"Verdana"])
        font7.setPointSize(10)
        font7.setBold(False)
        self.button_send_comm.setFont(font7)
        self.button_send_comm.setAutoFillBackground(False)

        self.horizontalLayout_11.addWidget(self.button_send_comm)


        self.verticalLayout.addLayout(self.horizontalLayout_11)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setFont(font1)
        self.tab_2.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.line_number_2 = QLabel(self.tab_2)
        self.line_number_2.setObjectName(u"line_number_2")
        sizePolicy2.setHeightForWidth(self.line_number_2.sizePolicy().hasHeightForWidth())
        self.line_number_2.setSizePolicy(sizePolicy2)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.line_number_2.setPalette(palette5)
        self.line_number_2.setFont(font2)
        self.line_number_2.setMouseTracking(True)
        self.line_number_2.setAutoFillBackground(False)
        self.line_number_2.setFrameShape(QFrame.NoFrame)
        self.line_number_2.setFrameShadow(QFrame.Plain)
        self.line_number_2.setLineWidth(0)
        self.line_number_2.setMidLineWidth(0)
        self.line_number_2.setTextFormat(Qt.AutoText)
        self.line_number_2.setScaledContents(False)
        self.line_number_2.setAlignment(Qt.AlignCenter)
        self.line_number_2.setMargin(0)
        self.line_number_2.setIndent(-1)

        self.horizontalLayout_12.addWidget(self.line_number_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.line_6 = QFrame(self.tab_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.model_box_2 = QComboBox(self.tab_2)
        self.model_box_2.setObjectName(u"model_box_2")
        sizePolicy2.setHeightForWidth(self.model_box_2.sizePolicy().hasHeightForWidth())
        self.model_box_2.setSizePolicy(sizePolicy2)
        self.model_box_2.setMinimumSize(QSize(350, 25))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette6.setBrush(QPalette.Active, QPalette.HighlightedText, brush7)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.model_box_2.setPalette(palette6)
        self.model_box_2.setFont(font3)
        self.model_box_2.setLayoutDirection(Qt.LeftToRight)
        self.model_box_2.setEditable(True)
        self.model_box_2.setCurrentText(u"")
        self.model_box_2.setMaxVisibleItems(20)
        self.model_box_2.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.model_box_2.setPlaceholderText(u"")

        self.horizontalLayout_14.addWidget(self.model_box_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.button_stop_2 = QPushButton(self.tab_2)
        self.button_stop_2.setObjectName(u"button_stop_2")
        self.button_stop_2.setMinimumSize(QSize(150, 50))
        self.button_stop_2.setMaximumSize(QSize(150, 50))
        self.button_stop_2.setFont(font4)
        self.button_stop_2.setAutoFillBackground(False)

        self.horizontalLayout_15.addWidget(self.button_stop_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_3)

        self.button_test_2 = QPushButton(self.tab_2)
        self.button_test_2.setObjectName(u"button_test_2")
        sizePolicy2.setHeightForWidth(self.button_test_2.sizePolicy().hasHeightForWidth())
        self.button_test_2.setSizePolicy(sizePolicy2)
        self.button_test_2.setMinimumSize(QSize(150, 50))
        self.button_test_2.setMaximumSize(QSize(150, 50))
        self.button_test_2.setFont(font4)
        self.button_test_2.setAutoFillBackground(False)
        self.button_test_2.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.button_test_2)

        self.button_work_2 = QPushButton(self.tab_2)
        self.button_work_2.setObjectName(u"button_work_2")
        sizePolicy2.setHeightForWidth(self.button_work_2.sizePolicy().hasHeightForWidth())
        self.button_work_2.setSizePolicy(sizePolicy2)
        self.button_work_2.setMinimumSize(QSize(150, 50))
        self.button_work_2.setMaximumSize(QSize(150, 50))
        self.button_work_2.setFont(font4)
        self.button_work_2.setAutoFillBackground(False)

        self.horizontalLayout_16.addWidget(self.button_work_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.defect_2 = QLabel(self.tab_2)
        self.defect_2.setObjectName(u"defect_2")
        sizePolicy2.setHeightForWidth(self.defect_2.sizePolicy().hasHeightForWidth())
        self.defect_2.setSizePolicy(sizePolicy2)
        self.defect_2.setMinimumSize(QSize(140, 35))
        self.defect_2.setFont(font5)
        self.defect_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.defect_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.main_pic_2 = QLabel(self.tab_2)
        self.main_pic_2.setObjectName(u"main_pic_2")
        sizePolicy2.setHeightForWidth(self.main_pic_2.sizePolicy().hasHeightForWidth())
        self.main_pic_2.setSizePolicy(sizePolicy2)
        self.main_pic_2.setMinimumSize(QSize(300, 300))
        self.main_pic_2.setMaximumSize(QSize(350, 350))
        self.main_pic_2.setStyleSheet(u"")
        self.main_pic_2.setFrameShape(QFrame.Box)
        self.main_pic_2.setLineWidth(1)
        self.main_pic_2.setScaledContents(True)
        self.main_pic_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.main_pic_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.comment_2 = QLabel(self.tab_2)
        self.comment_2.setObjectName(u"comment_2")
        sizePolicy2.setHeightForWidth(self.comment_2.sizePolicy().hasHeightForWidth())
        self.comment_2.setSizePolicy(sizePolicy2)
        self.comment_2.setMinimumSize(QSize(0, 0))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comment_2.setPalette(palette7)
        self.comment_2.setFont(font6)
        self.comment_2.setStyleSheet(u"")
        self.comment_2.setFrameShape(QFrame.NoFrame)
        self.comment_2.setLineWidth(0)
        self.comment_2.setMidLineWidth(0)
        self.comment_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.comment_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.text_send_2 = QTextEdit(self.tab_2)
        self.text_send_2.setObjectName(u"text_send_2")
        sizePolicy2.setHeightForWidth(self.text_send_2.sizePolicy().hasHeightForWidth())
        self.text_send_2.setSizePolicy(sizePolicy2)
        self.text_send_2.setMinimumSize(QSize(350, 70))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.text_send_2.setPalette(palette8)
        self.text_send_2.setFrameShape(QFrame.Box)
        self.text_send_2.setFrameShadow(QFrame.Plain)
        self.text_send_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.horizontalLayout_20.addWidget(self.text_send_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.button_send_comm_2 = QPushButton(self.tab_2)
        self.button_send_comm_2.setObjectName(u"button_send_comm_2")
        self.button_send_comm_2.setMinimumSize(QSize(150, 50))
        self.button_send_comm_2.setMaximumSize(QSize(150, 50))
        self.button_send_comm_2.setFont(font7)
        self.button_send_comm_2.setAutoFillBackground(False)

        self.horizontalLayout_21.addWidget(self.button_send_comm_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.model_box.setCurrentIndex(-1)
        self.model_box_2.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u043b\u0435\u0440\u0430", None))
        self.line_number_1.setText(QCoreApplication.translate("MainWindow", u"1-\u044f \u043b\u0438\u043d\u0438\u044f", None))
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0415\u0416\u0418\u041c \u041e\u0421\u0422\u0410\u041d\u041e\u0412", None))
        self.button_test.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0415\u0416\u0418\u041c \u0422\u0415\u0421\u0422", None))
        self.button_work.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0415\u0416\u0418\u041c \u0420\u0410\u0411\u041e\u0422\u0410", None))
        self.defect.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0418\u0413\u041d\u0410\u041b", None))
        self.main_pic.setText("")
        self.comment.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u041c\u041c\u0415\u041d\u0422\u0410\u0420\u0418\u0419", None))
        self.button_send_comm.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0422\u041f\u0420\u0410\u0412\u0418\u0422\u042c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u041b\u0418\u041d\u0418\u042f 1", None))
        self.line_number_2.setText(QCoreApplication.translate("MainWindow", u"2-\u044f \u043b\u0438\u043d\u0438\u044f", None))
        self.button_stop_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0415\u0416\u0418\u041c \u041e\u0421\u0422\u0410\u041d\u041e\u0412", None))
        self.button_test_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0415\u0416\u0418\u041c \u0422\u0415\u0421\u0422", None))
        self.button_work_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0415\u0416\u0418\u041c \u0420\u0410\u0411\u041e\u0422\u0410", None))
        self.defect_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0418\u0413\u041d\u0410\u041b", None))
        self.main_pic_2.setText("")
        self.comment_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u041c\u041c\u0415\u041d\u0422\u0410\u0420\u0418\u0419", None))
        self.button_send_comm_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0422\u041f\u0420\u0410\u0412\u0418\u0422\u042c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041b\u0418\u041d\u0418\u042f 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041b\u0418\u041d\u0418\u042f 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041b\u0418\u041d\u0418\u042f 4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u041b\u0418\u041d\u0418\u042f 5", None))
    # retranslateUi

