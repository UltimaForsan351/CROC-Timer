# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import interface_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1250, 200)
        MainWindow.setMinimumSize(QSize(1250, 200))
        MainWindow.setMaximumSize(QSize(1250, 16777215))
        self.StileSheet = QWidget(MainWindow)
        self.StileSheet.setObjectName(u"StileSheet")
        self.StileSheet.setMinimumSize(QSize(1250, 0))
        self.StileSheet.setStyleSheet(u"/*  CROC */\n"
"#CROC{\n"
"	color:rgba(255, 255, 255, 230)\n"
"\n"
"}\n"
"\n"
"\n"
"/*  combobox */\n"
"#comboBox{\n"
"	background-color: rgb(100, 100, 100);\n"
"	border-bottom: 2px solid rgba(0,164,96,255);\n"
"	border-radius: 8px;\n"
"	padding-left: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#comboBox::drop-down {\n"
"	border: transparent;\n"
"}\n"
"\n"
"#comboBox::down-arrow {\n"
"	image: url(:/Image/arrow-down-sign-to-navigate.png);\n"
"	wedth: 15px;\n"
"	height: 15px;\n"
"	margin-right: 4px;\n"
"}\n"
"\n"
"#comboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 2px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"#comboBox::on{ \n"
"	pass\n"
"}\n"
"\n"
"#comboBox QListView{\n"
"	outline: 0px;\n"
"	font-size: 10px;\n"
"	border-radius: 2px;\n"
"	padding: 5px;\n"
"	background-color: rgb(0, 164, 96);\n"
"}\n"
"\n"
"#comboBox QListView::item:!selected{\n"
"	padding-left: 2px;\n"
"	border-radius: 2px\n"
"}\n"
"\n"
"#comboBox QListView::item:hover{\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"\n"
""
                        "/*  Info\\ err */\n"
"#info{\n"
"	color: rgb(255, 143, 5);\n"
"}\n"
"\n"
"#err{\n"
"	\n"
"	color: rgb(231, 51, 51);\n"
"}\n"
"\n"
"\n"
"\n"
"/*  Clock */\n"
"#Clock{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/*  BG */\n"
"\n"
"#task_name_bd_bg, #hour_bg, #hour_bg_2, #hour_bg_3 {\n"
"	background-color: rgba(100,100,100,255);\n"
"	border-radius: 17px;\n"
"	border-bottom: 2px solid rgba(0,164,96,255);\n"
"}\n"
"\n"
"#contact_bg {\n"
"	border-radius: 10px;\n"
"	border-bottom: 2px solid rgba(0,164,96,255);\n"
"	background-color: rgba(100,100,100,255)\n"
"}\n"
"\n"
"#task_name_bd, #contact_name {\n"
"	color: rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"#hour_name{\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"#hour_name_2 {\n"
"	color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"#hour_name_3{\n"
"	color: rgb(170, 255, 0);\n"
"}\n"
"\n"
"#bg_down {\n"
"	background-color: rgb(220,236,230);\n"
"}\n"
"\n"
"#bg_down_1 {\n"
"	background-color: rgb(0,164,96);\n"
"	border-bottom-left-radius:7px;\n"
"	border-bottom-right-radius:7px;\n"
"}\n"
""
                        "\n"
"#bg_up {\n"
"	background-color: rgb(0,164,96);\n"
"	border-top-left-radius:7px;\n"
"	border-top-right-radius:7px\n"
"}\n"
"\n"
"#bg_left {\n"
"	background-color: rgb(0,164,96);\n"
"	\n"
"}\n"
"\n"
"#bg_mid {\n"
"	border-bottom-right-radius:7px;\n"
"	\n"
"}\n"
"\n"
"#page, #page_2, #page_3 {\n"
"	background-color: rgb(220,236,230);\n"
"	border-bottom-right-radius:7px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*  BTN Roll and accept\\delete */\n"
"\n"
"QPushButton#pushButton_time, QPushButton#pushButton_db, QPushButton#pushButton_contact, QPushButton#telegram_btn, QPushButton#iphone_btn {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#pushButton_time:hover, QPushButton#pushButton_db:hover, QPushButton#pushButton_contact:hover, QPushButton#telegram_btn:hover, QPushButton#iphone_btn:hover   {\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton#pushButton_time:pressed, QPushButton#pushButton_db:pressed, QPushButton#pushButton_contact:pressed, QPushButton#telegram_btn:pressed, QPushButton#iphone_btn:pressed  {\n"
"	padding-lef"
                        "t: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"\n"
"QPushButton#clouse_btn, QPushButton#delete_btn_1, QPushButton#delete_btn_2, QPushButton#delete_btn_3, QPushButton#delete_btn_4, QPushButton#delete_btn_5, QPushButton#accept_btn_1, QPushButton#accept_btn_2, QPushButton#accept_btn_3, QPushButton#accept_btn_4, QPushButton#accept_btn_5{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#clouse_btn:hover, QPushButton#delete_btn_1:hover, QPushButton#delete_btn_2:hover, QPushButton#delete_btn_3:hover, QPushButton#delete_btn_4:hover, QPushButton#delete_btn_5:hover, QPushButton#accept_btn_1:hover, QPushButton#accept_btn_2:hover, QPushButton#accept_btn_3:hover, QPushButton#accept_btn_4:hover, QPushButton#accept_btn_5:hover{\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton#clouse_btn:pressed, QPushButton#delete_btn_1:pressed, QPushButton#delete_btn_2:pressed, QPushButton#delete_btn_3:pressed, QPushButton#delete_btn_4:pressed, QPushButton#delete_btn_5:pressed, QPushButton#accept_btn_1:pressed, QPushButton#accept_btn_2:pres"
                        "sed, QPushButton#accept_btn_3:pressed, QPushButton#accept_btn_4:pressed, QPushButton#accept_btn_5:pressed{\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton#roll_btn{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#roll_btn:hover{\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton#roll_btn:pressed{\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"\n"
"/*  BTN  */\n"
"\n"
"QPushButton#start_btn_1, QPushButton#start_btn_2, QPushButton#start_btn_3, QPushButton#start_btn_4, QPushButton#start_btn_5, QPushButton#add_line_btn {\n"
"	background-color: qlineargradient(spread:pad, x1:0.0681818, y1:0.017, x2:1, y2:0, stop:0.267045 rgba(59, 193, 104, 255), stop:1 rgba(13, 162, 122, 255));\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton#start_btn_1:hover, QPushButton#start_btn_2:hover, QPushButton#start_btn_3:hover, QPushButton#start_btn_4:hover, QPushButton#start_btn_5:hover, QPushButton#add_line_btn:hover{\n"
"	border-radius: 6px;\n"
"	border: 2px solid "
                        "rgba(0, 0, 0, 255);\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton#start_btn_1:pressed, QPushButton#start_btn_2:pressed, QPushButton#start_btn_3:pressed, QPushButton#start_btn_4:pressed, QPushButton#start_btn_5:pressed, QPushButton#add_line_btn:pressed{\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 192, 112, 255), stop:1 rgba(0, 122, 0, 255));\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgba(0, 0, 0, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#stop_btn_1, QPushButton#stop_btn_2, QPushButton#stop_btn_3, QPushButton#stop_btn_4, QPushButton#stop_btn_5{\n"
"	background-color: qlineargradient(spread:pad, x1:0.0681818, y1:0.017, x2:1, y2:0, stop:0 rgba(232, 42, 42, 255), stop:1 rgba(176, 58, 58, 255));\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton#stop_btn_1:hover, QPushButton#stop_btn_2:hover, QPushButton#stop_btn_3:hover, QPushButton#stop_btn_4:hover, QPushButton#stop_btn_5"
                        ":hover{\n"
"	border-radius: 6px;\n"
"	border: 2px solid rgba(0, 0, 0, 255);\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton#stop_btn_1:pressed, QPushButton#stop_btn_2:pressed, QPushButton#stop_btn_3:pressed, QPushButton#stop_btn_4:pressed, QPushButton#stop_btn_5:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:0.0681818, y1:0.017, x2:1, y2:0.006, stop:0 rgba(198, 0, 0, 255), stop:1 rgba(72, 23, 23, 255));\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgba(0, 0, 0, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#pause_btn_1, QPushButton#pause_btn_2, QPushButton#pause_btn_3, QPushButton#pause_btn_4, QPushButton#pause_btn_5, QPushButton#remove_line_btn{\n"
"	background-color: qlineargradient(spread:pad, x1:0.0681818, y1:0.017, x2:1, y2:0, stop:0 rgba(230, 193, 81, 255), stop:1 rgba(210, 155, 74, 255));\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton#pause_btn_1:hover, QPushButton#pause_btn_2:hover, QPushButton#pa"
                        "use_btn_3:hover, QPushButton#pause_btn_4:hover, QPushButton#pause_btn_5:hover, QPushButton#remove_line_btn:hover{\n"
"	border-radius: 6px;\n"
"	border: 2px solid rgba(0, 0, 0, 255);\n"
"	padding-bottom: 4px;\n"
"}\n"
"\n"
"QPushButton#pause_btn_1:pressed, QPushButton#pause_btn_2:pressed, QPushButton#pause_btn_3:pressed, QPushButton#pause_btn_4:pressed, QPushButton#pause_btn_5:pressed, QPushButton#remove_line_btn:pressed {\n"
"	background-color:qlineargradient(spread:pad, x1:0.0681818, y1:0.017, x2:1, y2:0, stop:0 rgba(230, 173, 0, 255), stop:1 rgba(185, 110, 0, 255));\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgba(0, 0, 0, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*  Time BAR */\n"
"\n"
"\n"
"#bar_time_egg{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#bar_time_egg::chunk{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;;\n"
"	background-color: qli"
                        "neargradient(spread:pad, x1:0, y1:0, x2:0.676, y2:0, stop:0.0397727 rgba(0, 241, 81, 255), stop:1 rgba(174, 237, 0, 255));\n"
"}\n"
"\n"
"#bar_time_egg_2{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#bar_time_egg_2::chunk{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.676, y2:0, stop:0.0397727 rgba(0, 241, 81, 255), stop:1 rgba(174, 237, 0, 255));\n"
"}\n"
"\n"
"#bar_time_egg_3{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#bar_time_egg_3::chunk{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.676, y2:0, stop:0.0397727 rgba(0, 241, 81, 255), stop:1 rgba(174, 237, 0, 255));\n"
"}\n"
"\n"
"#bar_time_egg_4{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bo"
                        "ttom-right-radius:3px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#bar_time_egg_4::chunk{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.676, y2:0, stop:0.0397727 rgba(0, 241, 81, 255), stop:1 rgba(174, 237, 0, 255));\n"
"}\n"
"\n"
"#bar_time_egg_5{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#bar_time_egg_5::chunk{\n"
"	border-bottom-left-radius:3px;\n"
"	border-bottom-right-radius:3px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.676, y2:0, stop:0.0397727 rgba(0, 241, 81, 255), stop:1 rgba(174, 237, 0, 255));\n"
"}\n"
"\n"
"QTreeWidget {\n"
"	background-color: rgb(100, 100, 100);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	outline: none;\n"
"}\n"
"\n"
"\n"
"QTextEdit{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(100, 100, 100);\n"
"	color: rgb("
                        "255, 255, 255);\n"
"}\n"
"\n"
"\n"
"/*  VERTICAL SCROLLBAR  UG */\n"
"\n"
"\n"
"QScrollBar:horizontal{\n"
"	background-color: rgb(100, 100, 100);\n"
"	height: 5px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	background-color: rgb(100, 100, 100);\n"
"	width: 5px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: rgb(0, 164, 96);\n"
"	min-height: 30px;\n"
"	border-radius: 2px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{	\n"
"	background-color: rgb(255, 140, 0);\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(0, 164, 96);\n"
"	min-height: 30px;\n"
"	border-radius: 2px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{	\n"
"	background-color: rgb(255, 140, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgba(87, 94, 107,100"
                        ");\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgba(87, 94, 107,100);\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgba(87, 94, 107,100);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgba(87, 94, 107,100);\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	border:none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	border:none;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	border:none;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.StileSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg_up = QWidget(self.StileSheet)
        self.bg_up.setObjectName(u"bg_up")
        self.bg_up.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.bg_up)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.bg_up)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_24 = QHBoxLayout(self.widget)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_38 = QWidget(self.widget)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setMinimumSize(QSize(50, 0))
        self.widget_38.setMaximumSize(QSize(50, 16777215))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 1, 2, 1)
        self.delete_btn_1 = QPushButton(self.widget_38)
        self.delete_btn_1.setObjectName(u"delete_btn_1")
        self.delete_btn_1.setMinimumSize(QSize(24, 21))
        self.delete_btn_1.setMaximumSize(QSize(24, 21))
        self.delete_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_btn_1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Image/Clouse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn_1.setIcon(icon)
        self.delete_btn_1.setIconSize(QSize(15, 15))

        self.horizontalLayout_10.addWidget(self.delete_btn_1)

        self.accept_btn_1 = QPushButton(self.widget_38)
        self.accept_btn_1.setObjectName(u"accept_btn_1")
        self.accept_btn_1.setMinimumSize(QSize(24, 21))
        self.accept_btn_1.setMaximumSize(QSize(24, 21))
        self.accept_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.accept_btn_1.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Image/check-mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accept_btn_1.setIcon(icon1)
        self.accept_btn_1.setIconSize(QSize(15, 15))

        self.horizontalLayout_10.addWidget(self.accept_btn_1)


        self.horizontalLayout_24.addWidget(self.widget_38)

        self.widget_39 = QWidget(self.widget)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMinimumSize(QSize(500, 0))
        self.widget_39.setMaximumSize(QSize(500, 16777215))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_53 = QWidget(self.widget_39)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_14 = QVBoxLayout(self.widget_53)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.info = QLabel(self.widget_53)
        self.info.setObjectName(u"info")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.info.setFont(font)
        self.info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.info)


        self.horizontalLayout_9.addWidget(self.widget_53)

        self.widget_48 = QWidget(self.widget_39)
        self.widget_48.setObjectName(u"widget_48")
        self.verticalLayout_15 = QVBoxLayout(self.widget_48)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.err = QLabel(self.widget_48)
        self.err.setObjectName(u"err")
        self.err.setFont(font)
        self.err.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.err)


        self.horizontalLayout_9.addWidget(self.widget_48)


        self.horizontalLayout_24.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.widget)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(140, 0))
        self.widget_40.setMaximumSize(QSize(140, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.widget_40)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 2, 0, 2)
        self.CROC = QLabel(self.widget_40)
        self.CROC.setObjectName(u"CROC")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.CROC.setFont(font1)
        self.CROC.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.CROC)


        self.horizontalLayout_24.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.widget)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMinimumSize(QSize(180, 0))
        self.widget_41.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.widget_41)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(1, 1, 1, 1)

        self.horizontalLayout_24.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.widget)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_23 = QVBoxLayout(self.widget_42)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(2, 1, 2, 1)
        self.Clock = QLCDNumber(self.widget_42)
        self.Clock.setObjectName(u"Clock")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.Clock.setFont(font2)
        self.Clock.setFrameShape(QFrame.NoFrame)
        self.Clock.setSmallDecimalPoint(False)
        self.Clock.setMode(QLCDNumber.Dec)
        self.Clock.setSegmentStyle(QLCDNumber.Flat)
        self.Clock.setProperty("intValue", 0)

        self.verticalLayout_23.addWidget(self.Clock)


        self.horizontalLayout_24.addWidget(self.widget_42)


        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.bg_up)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(60, 20))
        self.widget_2.setMaximumSize(QSize(60, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 2, 0)
        self.roll_btn = QPushButton(self.widget_2)
        self.roll_btn.setObjectName(u"roll_btn")
        self.roll_btn.setMinimumSize(QSize(24, 21))
        self.roll_btn.setMaximumSize(QSize(24, 21))
        self.roll_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.roll_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/Image/circle_yellow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.roll_btn.setIcon(icon2)
        self.roll_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_3.addWidget(self.roll_btn)

        self.clouse_btn = QPushButton(self.widget_2)
        self.clouse_btn.setObjectName(u"clouse_btn")
        self.clouse_btn.setMinimumSize(QSize(24, 21))
        self.clouse_btn.setMaximumSize(QSize(24, 21))
        self.clouse_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clouse_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Image/circle_red.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clouse_btn.setIcon(icon3)
        self.clouse_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_3.addWidget(self.clouse_btn)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.bg_up)

        self.bg_down = QWidget(self.StileSheet)
        self.bg_down.setObjectName(u"bg_down")
        self.horizontalLayout = QHBoxLayout(self.bg_down)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg_left = QWidget(self.bg_down)
        self.bg_left.setObjectName(u"bg_left")
        self.bg_left.setMinimumSize(QSize(50, 180))
        self.bg_left.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.bg_left)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.bg_left)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_time = QPushButton(self.widget_5)
        self.pushButton_time.setObjectName(u"pushButton_time")
        self.pushButton_time.setMinimumSize(QSize(23, 23))
        self.pushButton_time.setMaximumSize(QSize(23, 23))
        self.pushButton_time.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Image/icon-time-management.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_time.setIcon(icon4)
        self.pushButton_time.setIconSize(QSize(22, 22))

        self.horizontalLayout_11.addWidget(self.pushButton_time)


        self.verticalLayout_8.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.bg_left)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_db = QPushButton(self.widget_6)
        self.pushButton_db.setObjectName(u"pushButton_db")
        self.pushButton_db.setMinimumSize(QSize(23, 23))
        self.pushButton_db.setMaximumSize(QSize(23, 23))
        self.pushButton_db.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Image/icon-database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_db.setIcon(icon5)
        self.pushButton_db.setIconSize(QSize(22, 22))

        self.horizontalLayout_12.addWidget(self.pushButton_db)


        self.verticalLayout_8.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.bg_left)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_contact = QPushButton(self.widget_7)
        self.pushButton_contact.setObjectName(u"pushButton_contact")
        self.pushButton_contact.setMinimumSize(QSize(23, 23))
        self.pushButton_contact.setMaximumSize(QSize(23, 23))
        icon6 = QIcon()
        icon6.addFile(u":/Image/icon-contact-us.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_contact.setIcon(icon6)
        self.pushButton_contact.setIconSize(QSize(22, 22))

        self.horizontalLayout_14.addWidget(self.pushButton_contact)


        self.verticalLayout_8.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.bg_left)

        self.bg_mid = QWidget(self.bg_down)
        self.bg_mid.setObjectName(u"bg_mid")
        self.verticalLayout_2 = QVBoxLayout(self.bg_mid)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.bg_mid)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_17 = QVBoxLayout(self.page)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 35))
        self.widget_3.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(500, 0))
        self.widget_8.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_4 = QVBoxLayout(self.widget_12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.line_login = QLineEdit(self.widget_12)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setMinimumSize(QSize(450, 25))
        self.line_login.setMaximumSize(QSize(500, 25))
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(10)
        self.line_login.setFont(font3)
        self.line_login.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);\n"
"border: none;\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.line_login.setClearButtonEnabled(False)

        self.verticalLayout_4.addWidget(self.line_login)


        self.verticalLayout_3.addWidget(self.widget_12)


        self.horizontalLayout_4.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(140, 0))
        self.widget_9.setMaximumSize(QSize(140, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.Time_1 = QLabel(self.widget_9)
        self.Time_1.setObjectName(u"Time_1")
        self.Time_1.setMinimumSize(QSize(100, 20))
        self.Time_1.setMaximumSize(QSize(150, 20))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.Time_1.setFont(font4)
        self.Time_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.Time_1)


        self.horizontalLayout_4.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(180, 0))
        self.widget_10.setMaximumSize(QSize(180, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(self.widget_10)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.widget_49)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_32.setSpacing(1)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(1, 1, 1, 1)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Bahnschrift")
        font5.setPointSize(12)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_6)


        self.horizontalLayout_13.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget_49)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_33.setSpacing(1)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(1, 1, 1, 1)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_7)


        self.horizontalLayout_13.addWidget(self.frame_4)


        self.horizontalLayout_6.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.widget_10)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.widget_50)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_34.setSpacing(1)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(1, 1, 1, 1)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.label_8)


        self.horizontalLayout_17.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.widget_50)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(1, 1, 1, 1)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_9)


        self.horizontalLayout_17.addWidget(self.frame_5)


        self.horizontalLayout_6.addWidget(self.widget_50)

        self.widget_51 = QWidget(self.widget_10)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.widget_51)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_36.setSpacing(1)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(1, 1, 1, 1)
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_10)


        self.horizontalLayout_21.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.widget_51)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(1, 1, 1, 1)
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_11)


        self.horizontalLayout_21.addWidget(self.frame_7)


        self.horizontalLayout_6.addWidget(self.widget_51)


        self.horizontalLayout_4.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.pause_btn_1 = QPushButton(self.widget_11)
        self.pause_btn_1.setObjectName(u"pause_btn_1")
        self.pause_btn_1.setMinimumSize(QSize(140, 25))
        self.pause_btn_1.setMaximumSize(QSize(140, 25))
        self.pause_btn_1.setFont(font2)
        self.pause_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pause_btn_1.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/image/free-icon-font-user2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_btn_1.setIcon(icon7)
        self.pause_btn_1.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pause_btn_1)

        self.stop_btn_1 = QPushButton(self.widget_11)
        self.stop_btn_1.setObjectName(u"stop_btn_1")
        self.stop_btn_1.setMinimumSize(QSize(80, 25))
        self.stop_btn_1.setMaximumSize(QSize(80, 25))
        self.stop_btn_1.setFont(font2)
        self.stop_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_btn_1.setStyleSheet(u"")
        self.stop_btn_1.setIcon(icon7)
        self.stop_btn_1.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.stop_btn_1)

        self.start_btn_1 = QPushButton(self.widget_11)
        self.start_btn_1.setObjectName(u"start_btn_1")
        self.start_btn_1.setMinimumSize(QSize(140, 25))
        self.start_btn_1.setMaximumSize(QSize(140, 25))
        self.start_btn_1.setFont(font2)
        self.start_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_btn_1.setStyleSheet(u"")
        self.start_btn_1.setIcon(icon7)
        self.start_btn_1.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.start_btn_1)


        self.horizontalLayout_4.addWidget(self.widget_11)


        self.verticalLayout_17.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 35))
        self.widget_4.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_4)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(500, 0))
        self.widget_14.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget_14)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = QWidget(self.widget_14)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_7 = QVBoxLayout(self.widget_31)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.line_login_2 = QLineEdit(self.widget_31)
        self.line_login_2.setObjectName(u"line_login_2")
        self.line_login_2.setMinimumSize(QSize(450, 25))
        self.line_login_2.setMaximumSize(QSize(500, 25))
        self.line_login_2.setFont(font3)
        self.line_login_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);\n"
"border: none;\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.line_login_2.setClearButtonEnabled(False)

        self.verticalLayout_7.addWidget(self.line_login_2)


        self.verticalLayout_6.addWidget(self.widget_31)


        self.horizontalLayout_8.addWidget(self.widget_14)

        self.widget_33 = QWidget(self.widget_4)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(140, 0))
        self.widget_33.setMaximumSize(QSize(140, 16777215))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.Time_2 = QLabel(self.widget_33)
        self.Time_2.setObjectName(u"Time_2")
        self.Time_2.setMinimumSize(QSize(100, 20))
        self.Time_2.setMaximumSize(QSize(150, 20))
        self.Time_2.setFont(font4)
        self.Time_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.Time_2)


        self.horizontalLayout_8.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.widget_4)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(180, 0))
        self.widget_34.setMaximumSize(QSize(180, 16777215))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_52 = QWidget(self.widget_34)
        self.widget_52.setObjectName(u"widget_52")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.widget_52)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_38.setSpacing(1)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(1, 1, 1, 1)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_12)


        self.horizontalLayout_29.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.widget_52)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_39.setSpacing(1)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(1, 1, 1, 1)
        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.label_13)


        self.horizontalLayout_29.addWidget(self.frame_10)


        self.horizontalLayout_28.addWidget(self.widget_52)

        self.widget_54 = QWidget(self.widget_34)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.widget_54)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_40.setSpacing(1)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(1, 1, 1, 1)
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_14)


        self.horizontalLayout_30.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.widget_54)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(1, 1, 1, 1)
        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_15)


        self.horizontalLayout_30.addWidget(self.frame_12)


        self.horizontalLayout_28.addWidget(self.widget_54)

        self.widget_55 = QWidget(self.widget_34)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.widget_55)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_42.setSpacing(1)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(1, 1, 1, 1)
        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.label_16)


        self.horizontalLayout_31.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.widget_55)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(1, 1, 1, 1)
        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_17)


        self.horizontalLayout_31.addWidget(self.frame_14)


        self.horizontalLayout_28.addWidget(self.widget_55)


        self.horizontalLayout_8.addWidget(self.widget_34)

        self.widget_35 = QWidget(self.widget_4)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_44.setSpacing(5)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(2, 2, 2, 2)
        self.pause_btn_2 = QPushButton(self.widget_35)
        self.pause_btn_2.setObjectName(u"pause_btn_2")
        self.pause_btn_2.setMinimumSize(QSize(140, 25))
        self.pause_btn_2.setMaximumSize(QSize(140, 25))
        self.pause_btn_2.setFont(font2)
        self.pause_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pause_btn_2.setStyleSheet(u"")
        self.pause_btn_2.setIcon(icon7)
        self.pause_btn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_44.addWidget(self.pause_btn_2)

        self.stop_btn_2 = QPushButton(self.widget_35)
        self.stop_btn_2.setObjectName(u"stop_btn_2")
        self.stop_btn_2.setMinimumSize(QSize(80, 25))
        self.stop_btn_2.setMaximumSize(QSize(80, 25))
        self.stop_btn_2.setFont(font2)
        self.stop_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_btn_2.setStyleSheet(u"")
        self.stop_btn_2.setIcon(icon7)
        self.stop_btn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_44.addWidget(self.stop_btn_2)

        self.start_btn_2 = QPushButton(self.widget_35)
        self.start_btn_2.setObjectName(u"start_btn_2")
        self.start_btn_2.setMinimumSize(QSize(140, 25))
        self.start_btn_2.setMaximumSize(QSize(140, 25))
        self.start_btn_2.setFont(font2)
        self.start_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_btn_2.setStyleSheet(u"")
        self.start_btn_2.setIcon(icon7)
        self.start_btn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_44.addWidget(self.start_btn_2)


        self.horizontalLayout_8.addWidget(self.widget_35)


        self.verticalLayout_17.addWidget(self.widget_4)

        self.widget_30 = QWidget(self.page)
        self.widget_30.setObjectName(u"widget_30")

        self.verticalLayout_17.addWidget(self.widget_30)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.page_3)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(0, 30))
        self.widget_26.setMaximumSize(QSize(16777215, 30))
        self.verticalLayout_13 = QVBoxLayout(self.widget_26)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(290, 0, 0, 0)
        self.contact_bg = QWidget(self.widget_26)
        self.contact_bg.setObjectName(u"contact_bg")
        self.contact_bg.setMinimumSize(QSize(600, 25))
        self.contact_bg.setMaximumSize(QSize(600, 25))
        self.contact_bg.setStyleSheet(u"")
        self.verticalLayout_70 = QVBoxLayout(self.contact_bg)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.contact_name = QLabel(self.contact_bg)
        self.contact_name.setObjectName(u"contact_name")
        self.contact_name.setMinimumSize(QSize(0, 25))
        self.contact_name.setMaximumSize(QSize(16777215, 25))
        font6 = QFont()
        font6.setFamily(u"Tahoma")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.contact_name.setFont(font6)
        self.contact_name.setStyleSheet(u"border-top: transparent;\n"
"border-bottom: transparent;\n"
"border-left: transparent;\n"
"border-right: transparent;\n"
"background-color: transparent;")
        self.contact_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.contact_name)


        self.verticalLayout_13.addWidget(self.contact_bg)


        self.verticalLayout_12.addWidget(self.widget_26)

        self.widget_25 = QWidget(self.page_3)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMaximumSize(QSize(1200, 75))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(400, 50))
        self.widget_27.setMaximumSize(QSize(400, 50))

        self.horizontalLayout_23.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_25)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(400, 50))
        self.widget_28.setMaximumSize(QSize(400, 50))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 2, 0, 2)
        self.telegram_btn = QPushButton(self.widget_28)
        self.telegram_btn.setObjectName(u"telegram_btn")
        self.telegram_btn.setMinimumSize(QSize(40, 40))
        self.telegram_btn.setMaximumSize(QSize(40, 40))
        self.telegram_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/Image/free-icon-telegram-3536705.png", QSize(), QIcon.Normal, QIcon.Off)
        self.telegram_btn.setIcon(icon8)
        self.telegram_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_25.addWidget(self.telegram_btn)

        self.iphone_btn = QPushButton(self.widget_28)
        self.iphone_btn.setObjectName(u"iphone_btn")
        self.iphone_btn.setMinimumSize(QSize(40, 40))
        self.iphone_btn.setMaximumSize(QSize(40, 40))
        self.iphone_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/Image/free-icon-telephone-symbol-button-25377.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iphone_btn.setIcon(icon9)
        self.iphone_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_25.addWidget(self.iphone_btn)


        self.horizontalLayout_23.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_25)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_29)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_26.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(295, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer)


        self.horizontalLayout_23.addWidget(self.widget_29)


        self.verticalLayout_12.addWidget(self.widget_25)

        self.widget_36 = QWidget(self.page_3)
        self.widget_36.setObjectName(u"widget_36")

        self.verticalLayout_12.addWidget(self.widget_36)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_18 = QVBoxLayout(self.page_2)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_37 = QWidget(self.page_2)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMaximumSize(QSize(1200, 90))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_37)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(250, 0))
        self.widget_15.setMaximumSize(QSize(250, 16777215))
        self.widget_15.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 0, 5, 0)
        self.comboBox = QComboBox(self.widget_15)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 25))
        font7 = QFont()
        font7.setFamily(u"Tahoma")
        font7.setBold(True)
        font7.setWeight(75)
        self.comboBox.setFont(font7)
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox.setDuplicatesEnabled(True)

        self.horizontalLayout_16.addWidget(self.comboBox)


        self.horizontalLayout_15.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_37)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(450, 0))
        self.widget_16.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.widget_16)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 10, 5, -1)
        self.task_name_bd_bg = QWidget(self.widget_16)
        self.task_name_bd_bg.setObjectName(u"task_name_bd_bg")
        self.task_name_bd_bg.setMinimumSize(QSize(0, 35))
        self.task_name_bd_bg.setMaximumSize(QSize(16777215, 35))
        self.task_name_bd_bg.setStyleSheet(u"")
        self.verticalLayout_66 = QVBoxLayout(self.task_name_bd_bg)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(2, 2, 2, 2)
        self.task_name_bd = QLabel(self.task_name_bd_bg)
        self.task_name_bd.setObjectName(u"task_name_bd")
        self.task_name_bd.setFont(font2)
        self.task_name_bd.setStyleSheet(u"border-top: transparent;\n"
"border-bottom: transparent;\n"
"border-left: transparent;\n"
"border-right: transparent;\n"
"background-color: transparent;")
        self.task_name_bd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_66.addWidget(self.task_name_bd)


        self.verticalLayout_9.addWidget(self.task_name_bd_bg)


        self.horizontalLayout_15.addWidget(self.widget_16)

        self.widget_18 = QWidget(self.widget_37)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_18)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.hour_bg = QWidget(self.widget_17)
        self.hour_bg.setObjectName(u"hour_bg")
        self.hour_bg.setMinimumSize(QSize(40, 40))
        self.hour_bg.setMaximumSize(QSize(40, 40))
        self.hour_bg.setStyleSheet(u"")
        self.verticalLayout_67 = QVBoxLayout(self.hour_bg)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.hour_name = QLabel(self.hour_bg)
        self.hour_name.setObjectName(u"hour_name")
        self.hour_name.setMinimumSize(QSize(40, 40))
        self.hour_name.setMaximumSize(QSize(40, 40))
        self.hour_name.setFont(font2)
        self.hour_name.setStyleSheet(u"border-top: transparent;\n"
"border-bottom: transparent;\n"
"border-left: transparent;\n"
"border-right: transparent;\n"
"background-color: transparent;")
        self.hour_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.hour_name)


        self.horizontalLayout_19.addWidget(self.hour_bg)


        self.horizontalLayout_18.addWidget(self.widget_17)

        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_10 = QVBoxLayout(self.widget_19)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.widget_19)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-1)

        self.verticalLayout_10.addWidget(self.label)


        self.horizontalLayout_18.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_18)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_5 = QGridLayout(self.widget_20)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.hour_bg_2 = QWidget(self.widget_20)
        self.hour_bg_2.setObjectName(u"hour_bg_2")
        self.hour_bg_2.setMinimumSize(QSize(40, 40))
        self.hour_bg_2.setMaximumSize(QSize(40, 40))
        self.hour_bg_2.setStyleSheet(u"")
        self.verticalLayout_68 = QVBoxLayout(self.hour_bg_2)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.hour_name_2 = QLabel(self.hour_bg_2)
        self.hour_name_2.setObjectName(u"hour_name_2")
        self.hour_name_2.setMinimumSize(QSize(40, 40))
        self.hour_name_2.setMaximumSize(QSize(40, 40))
        self.hour_name_2.setFont(font2)
        self.hour_name_2.setStyleSheet(u"border-top: transparent;\n"
"border-bottom: transparent;\n"
"border-left: transparent;\n"
"border-right: transparent;\n"
"background-color: transparent;")
        self.hour_name_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.hour_name_2)


        self.gridLayout_5.addWidget(self.hour_bg_2, 0, 0, 1, 1)


        self.horizontalLayout_18.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget_18)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.widget_21)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_11 = QVBoxLayout(self.widget_24)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.widget_24)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(-1)

        self.verticalLayout_11.addWidget(self.label_2)


        self.horizontalLayout_20.addWidget(self.widget_24)


        self.horizontalLayout_18.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.widget_18)
        self.widget_22.setObjectName(u"widget_22")
        self.gridLayout_6 = QGridLayout(self.widget_22)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.hour_bg_3 = QWidget(self.widget_22)
        self.hour_bg_3.setObjectName(u"hour_bg_3")
        self.hour_bg_3.setMinimumSize(QSize(40, 40))
        self.hour_bg_3.setMaximumSize(QSize(40, 40))
        self.hour_bg_3.setStyleSheet(u"")
        self.verticalLayout_69 = QVBoxLayout(self.hour_bg_3)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.hour_name_3 = QLabel(self.hour_bg_3)
        self.hour_name_3.setObjectName(u"hour_name_3")
        self.hour_name_3.setMinimumSize(QSize(40, 40))
        self.hour_name_3.setMaximumSize(QSize(40, 40))
        self.hour_name_3.setFont(font2)
        self.hour_name_3.setStyleSheet(u"border-top: transparent;\n"
"border-bottom: transparent;\n"
"border-left: transparent;\n"
"border-right: transparent;\n"
"background-color: transparent;")
        self.hour_name_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.hour_name_3)


        self.gridLayout_6.addWidget(self.hour_bg_3, 0, 0, 1, 1)


        self.horizontalLayout_18.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.widget_18)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_23)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setIndent(-1)

        self.horizontalLayout_22.addWidget(self.label_3)


        self.horizontalLayout_18.addWidget(self.widget_23)


        self.horizontalLayout_15.addWidget(self.widget_18)


        self.verticalLayout_18.addWidget(self.widget_37)

        self.widget_43 = QWidget(self.page_2)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.widget_44 = QWidget(self.widget_43)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setMinimumSize(QSize(600, 0))
        self.widget_44.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.widget_44)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_46 = QWidget(self.widget_44)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(20, 5, 20, 5)
        self.coment_view = QTextEdit(self.widget_46)
        self.coment_view.setObjectName(u"coment_view")
        font8 = QFont()
        font8.setFamily(u"Tahoma")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.coment_view.setFont(font8)
        self.coment_view.setAutoFillBackground(False)
        self.coment_view.setAutoFormatting(QTextEdit.AutoAll)
        self.coment_view.setTabChangesFocus(True)
        self.coment_view.setLineWrapColumnOrWidth(1)
        self.coment_view.setReadOnly(True)
        self.coment_view.setOverwriteMode(False)
        self.coment_view.setTabStopWidth(100)
        self.coment_view.setCursorWidth(1)

        self.horizontalLayout_48.addWidget(self.coment_view)


        self.verticalLayout_19.addWidget(self.widget_46)


        self.horizontalLayout_45.addWidget(self.widget_44)

        self.widget_45 = QWidget(self.widget_43)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(600, 0))
        self.widget_45.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.widget_45)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_56 = QWidget(self.widget_45)
        self.widget_56.setObjectName(u"widget_56")
        self.gridLayout_3 = QGridLayout(self.widget_56)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(20, 5, 20, 5)
        self.comentEdit = QTextEdit(self.widget_56)
        self.comentEdit.setObjectName(u"comentEdit")
        self.comentEdit.setFont(font8)
        self.comentEdit.setAutoFillBackground(False)
        self.comentEdit.setAutoFormatting(QTextEdit.AutoAll)
        self.comentEdit.setTabChangesFocus(True)
        self.comentEdit.setLineWrapColumnOrWidth(1)
        self.comentEdit.setOverwriteMode(False)
        self.comentEdit.setTabStopWidth(100)
        self.comentEdit.setCursorWidth(1)

        self.gridLayout_3.addWidget(self.comentEdit, 0, 0, 1, 1)


        self.verticalLayout_22.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.widget_45)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setMinimumSize(QSize(0, 40))
        self.widget_57.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_4 = QGridLayout(self.widget_57)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(60, 5, 60, 5)
        self.add_line_btn = QPushButton(self.widget_57)
        self.add_line_btn.setObjectName(u"add_line_btn")
        self.add_line_btn.setMinimumSize(QSize(100, 25))
        font9 = QFont()
        font9.setFamily(u"Bookman Old Style")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.add_line_btn.setFont(font9)
        self.add_line_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.add_line_btn, 0, 0, 1, 1)


        self.verticalLayout_22.addWidget(self.widget_57)


        self.horizontalLayout_45.addWidget(self.widget_45)


        self.verticalLayout_18.addWidget(self.widget_43)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.bg_mid)


        self.verticalLayout.addWidget(self.bg_down)

        self.bg_down_1 = QWidget(self.StileSheet)
        self.bg_down_1.setObjectName(u"bg_down_1")
        self.bg_down_1.setMinimumSize(QSize(0, 10))
        self.bg_down_1.setMaximumSize(QSize(16777215, 10))
        self.horizontalLayout_46 = QHBoxLayout(self.bg_down_1)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.widget_58 = QWidget(self.bg_down_1)
        self.widget_58.setObjectName(u"widget_58")

        self.horizontalLayout_46.addWidget(self.widget_58)

        self.widget_59 = QWidget(self.bg_down_1)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_60 = QWidget(self.widget_59)
        self.widget_60.setObjectName(u"widget_60")

        self.horizontalLayout_47.addWidget(self.widget_60)

        self.resize_window = QWidget(self.widget_59)
        self.resize_window.setObjectName(u"resize_window")
        self.resize_window.setMinimumSize(QSize(16, 0))
        self.resize_window.setMaximumSize(QSize(16, 16777215))

        self.horizontalLayout_47.addWidget(self.resize_window)


        self.horizontalLayout_46.addWidget(self.widget_59)


        self.verticalLayout.addWidget(self.bg_down_1)

        MainWindow.setCentralWidget(self.StileSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CROC Timer", None))
        self.delete_btn_1.setText("")
        self.accept_btn_1.setText("")
        self.info.setText("")
        self.err.setText("")
        self.CROC.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0420\u041e\u041a", None))
        self.roll_btn.setText("")
        self.clouse_btn.setText("")
        self.pushButton_time.setText("")
        self.pushButton_db.setText("")
        self.pushButton_contact.setText("")
        self.line_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Task Name", None))
        self.Time_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pause_btn_1.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stop_btn_1.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.start_btn_1.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.line_login_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Task Name", None))
        self.Time_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pause_btn_2.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stop_btn_2.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.start_btn_2.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.contact_name.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u043d\u0430\u043c\u0438 + \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044e", None))
        self.telegram_btn.setText("")
        self.iphone_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"by UltimaForsan", None))
#if QT_CONFIG(accessibility)
        self.widget_15.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.task_name_bd.setText(QCoreApplication.translate("MainWindow", u"Task name", None))
        self.hour_name.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441(\u043e\u0432)", None))
        self.hour_name_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0443\u0442", None))
        self.hour_name_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043a\u0443\u043d\u0434", None))
        self.coment_view.setDocumentTitle("")
        self.comentEdit.setDocumentTitle("")
        self.add_line_btn.setText(QCoreApplication.translate("MainWindow", u"Commit comment", None))
    # retranslateUi

