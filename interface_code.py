##############################################################################
####Imports###
from PySide2 import QtCore, QtWidgets, QtGui
import sys,os
import sqlite3 as sl
import datetime as dt
from threading import *
import webbrowser
##############################################################################
####Imports Fix###
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
##############################################################################
###Import interface file###
from interface_ui import *
##############################################################################
###Main class###
class MainWindow(QMainWindow):
    ###############################################################################
    ###FUNCTIONS###        
    ###############################################################################
    ###DAta Base###
    def db_check(self):
        self.con = sl.connect('tasktime.db')
        with self.con:
            # получаем количество таблиц с нужным нам именем
            self.table = self.con.execute("select count(*) from sqlite_master where type='table' and name='bd'")
            for self.row in self.table:
                # если таких таблиц нет
                if self.row[0] == 0:
                    with self.con:
                        self.con.execute("""
                            CREATE TABLE bd (
                            task VARCHAR(30) PRIMARY KEY,
                            hour INTEGER,
                            min INTEGER,
                            sec INTEGER,
                            comment VARCHAR(9999)                       
                    );
                        """)
                else:
                    pass
        self.con.close()
    def url_telegram(self):
        webbrowser.open('https://t.me/Nikolay_BMW', new=2)
    ###############################################################################
    ###start btn###
    def starttime(self):
        self.flag = True
    def starttime_1(self):
        self.flag_1 = True
    ###############################################################################
    ###stop btn###
    def stoptime(self):
        self.flag = False
        self.count = 0
        self.update_db_data()
    def stoptime_1(self):
        self.flag_1 = False
        self.count_1 = 0
        self.update_db_data_1()
    ###############################################################################
    ###pause btn###
    def pausetime(self):
        self.flag = False
    def pausetime_1(self):
        self.flag_1 = False
    ###############################################################################
    ###Task DB###    
    def createTask(self):
        self.flag2 = False
        self.pot = 0
        self.con = sl.connect('tasktime.db')
        self.cursorDB = self.con.cursor()
        self.task_name_1 = self.ui.line_login.text()

        self.cursorDB.execute("SELECT task FROM bd")
        self.results = self.cursorDB.fetchall()
    
        for self.e in self.results:
            if self.e[0] == self.task_name_1:
                self.ui.info.setText(("INFO: Task already exists"))
                self.pot = 1
                break
            else:
                pass
        if self.pot == 1:
            self.flag2 = True
        else:
            self.dataAll = []
            self.dataAll.append(self.task_name_1)  
            self.dataAll.append(self.all_h_1)
            self.dataAll.append(self.all_min_1)
            self.dataAll.append(self.all_sec_1)
            #подготавливаем множественный запрос
            self.sql = 'INSERT INTO bd(task, hour, min, sec) values(?, ?, ?, ?)'
            #отправка данных
            with self.con:
                self.con.execute(self.sql, self.dataAll)
                self.flag2 = False
    def createTask_1(self):
        self.flag2_1 = False
        self.pot_1 = 0
        self.con = sl.connect('tasktime.db')
        self.cursorDB = self.con.cursor()
        self.task_name_1_1 = self.ui.line_login_2.text()

        self.cursorDB.execute("SELECT task FROM bd")
        self.results_1 = self.cursorDB.fetchall()
    
        for self.e in self.results_1:
            if self.e[0] == self.task_name_1_1:
                self.ui.info.setText(("INFO: Task already exists"))
                self.pot_1 = 1
                break
            else:
                pass
        if self.pot_1 == 1:
            self.flag2_1 = True
        else:
            self.dataAll_1 = []
            self.dataAll_1.append(self.task_name_1_1)  
            self.dataAll_1.append(self.all_h_1_1)
            self.dataAll_1.append(self.all_min_1_1)
            self.dataAll_1.append(self.all_sec_1_1)
            #подготавливаем множественный запрос
            self.sql = 'INSERT INTO bd(task, hour, min, sec) values(?, ?, ?, ?)'
            #отправка данных
            with self.con:
                self.con.execute(self.sql, self.dataAll_1)
                self.flag2_1 = False
    ###############################################################################
    ###print DB data###
    def print_db_data(self):
        self.con = sl.connect('tasktime.db')
        with self.con:
            # получаем количество таблиц с нужным нам именем
            self.table = self.con.execute("select count(*) from sqlite_master where type='table' and name='bd'")
            for self.row in self.table:
                # если таких таблиц нет
                if self.row[0] == 0:
                    self.db_check()
                else:
                    self.con = sl.connect('tasktime.db')
                    self.cursorDB = self.con.cursor()
                    self.cursorDB.execute('SELECT task FROM bd')
                    self.aa = self.ui.comboBox.currentText()
                    self.results_all_name_tasks = self.cursorDB.fetchall()
                    self.ui.comboBox.clear()
                    for self.name in self.results_all_name_tasks:
                        self.ui.comboBox.addItem(str(self.name[0]))          
        self.con.close()
    ###############################################################################
    ###change box view###
    def change(self):
        self.aa = self.ui.comboBox.currentText()
        if self.aa != '':
            self.conn = sl.connect('tasktime.db')
            self.cursorcheck = self.conn.cursor()
            self.cursorcheck.execute('SELECT hour, min, sec, comment FROM bd WHERE task = ?', (self.aa,))
            self.check_task_time = self.cursorcheck.fetchall()
            for self.z in self.check_task_time:
                self.param_1 = str(self.z[0])
                self.param_2 = str(self.z[1])
                self.param_3 = str(self.z[2])
                self.param_4 = str(self.z[3])
            self.ui.task_name_bd.setText(self.aa)
            self.ui.hour_name.setText(self.param_1)
            self.ui.hour_name_2.setText(self.param_2)
            self.ui.hour_name_3.setText(self.param_3)
            self.ui.coment_view.setText(self.param_4)
            if not self.ui.comentEdit.toPlainText():
                self.ui.comentEdit.setText(self.param_4)
                self.task_for_update_coment = self.aa
            self.con.close()
        else:
            pass
    ###############################################################################
    ###Commit coment BTN###     
    def commit_comment(self):
        self.none_text = str("")
        self.bb = self.ui.comentEdit.toPlainText()
        self.conn = sl.connect('tasktime.db')
        self.cursor_commit = self.conn.cursor()
        if self.bb != '':
            self.cursor_commit.execute('UPDATE bd SET comment = ? WHERE task = ?', (self.bb, self.task_for_update_coment))
            self.ui.comentEdit.clear()
            self.ui.coment_view.clear()
        else:
            self.cursor_commit.execute('UPDATE bd SET comment = ? WHERE task = ?', (self.none_text, self.task_for_update_coment))
            self.ui.comentEdit.clear()
            self.ui.coment_view.clear()
        ###Disconnect#
        self.conn.commit()
        self.conn.close()
    ###############################################################################
    ###Task DB update### 
    def update_db_data(self):
        ###Sellect data###
        self.pott = 0
        self.db_check()
        self.createTask()
        self.con = sl.connect('tasktime.db')
        self.cursorDB = self.con.cursor()
        self.task_name_for_update = self.ui.line_login.text()

        self.cursorDB.execute("SELECT task FROM bd")
        self.results = self.cursorDB.fetchall()

        if self.flag2 == True:
            if self.task_name_for_update == '':
                self.ui.err.setText("EROR: Enter the name")
                return
            else:
                self.ui.err.setText("")  
                self.cursorDB.execute('SELECT hour, min, sec FROM bd WHERE task = ?', (self.task_name_for_update,))
                self.results_new = self.cursorDB.fetchall()
                for self.o in self.results_new:
                    self.new_h_1 = self.o[0]
                    self.new_min_1 = self.o[1]
                    self.new_sec_1 = self.o[2]

                self.parm3 = int(self.all_sec_1) + int(self.new_sec_1)

                if self.parm3 >= 60:
                    self.seconds = self.parm3
                    self.seconds = self.seconds % (24 * 3600)
                    self.hour = self.seconds // 3600
                    self.seconds %= 3600
                    self.minutes = self.seconds // 60
                    self.seconds %= 60
                    self.other_time_1 = ("%d:%02d:%02d" % (self.hour, self.minutes, self.seconds))
                    self.xy = self.other_time_1.split(':')

                    self.cursorDB.execute('UPDATE bd SET sec = ? WHERE task = ?', (self.xy[2], self.task_name_for_update))
                    self.cursorDB.execute('UPDATE bd SET min = ? WHERE task = ?', (int(self.new_min_1) + int(self.xy[1]), self.task_name_for_update))
                    self.cursorDB.execute('UPDATE bd SET hour = ? WHERE task = ?', (int(self.new_h_1) + int(self.xy[0]), self.task_name_for_update))
                    
                    self.cursorDB.execute('SELECT hour, min, sec FROM bd WHERE task = ?', (self.task_name_for_update,))
                else:
                    self.cursorDB.execute('UPDATE bd SET sec = ? WHERE task = ?', (self.parm3, self.task_name_for_update))

                self.cursorDB.execute('SELECT hour, min, sec FROM bd WHERE task = ?', (self.task_name_for_update,))
                self.results_new = self.cursorDB.fetchall()
                for self.o in self.results_new:
                    self.new_min_1 = int(self.o[1])
                    
                self.parm2 = int(self.all_min_1) + int(self.new_min_1)

                if self.parm2 >= 60: 
                    self.min = self.parm2
                    self.min = self.min % (24*3600)
                    self.Hour = self.min // 60
                    self.min %= 60
                    self.other_time_1 = ("%d:%d" % (self.Hour, self.min))
                    self.xu = self.other_time_1.split(':')

                    self.cursorDB.execute('UPDATE bd SET min = ? WHERE task = ?', (int(self.xu[1]), self.task_name_for_update))
                    self.cursorDB.execute('UPDATE bd SET hour = ? WHERE task = ?', (int(self.new_h_1) + int(self.xu[0]), self.task_name_for_update))
                else:
                    self.cursorDB.execute('UPDATE bd SET min = ? WHERE task = ?', (self.parm2, self.task_name_for_update))

                self.cursorDB.execute('SELECT hour, min, sec FROM bd WHERE task = ?', (self.task_name_for_update,))
                self.results_new = self.cursorDB.fetchall()
                for self.o in self.results_new:
                    self.new_h_1 = int(self.o[0])
                self.parm1 = int(self.all_h_1) + int(self.new_h_1)       
                self.cursorDB.execute('UPDATE bd SET hour = ? WHERE task = ?', (self.parm1, self.task_name_for_update))
        else:
            pass
        ###Disconnect#
        self.con.commit()
        self.con.close()
    def update_db_data_1(self):
        ###Sellect data###
        self.pott = 0
        self.db_check()
        self.createTask_1()
        self.con = sl.connect('tasktime.db')
        self.cursorDB = self.con.cursor()
        self.task_name_for_update_1 = self.ui.line_login_2.text()
        self.cursorDB.execute("SELECT task FROM bd")
        self.results_1 = self.cursorDB.fetchall()

        if self.flag2_1 == True:
            if self.task_name_for_update_1 == '':
                self.ui.err.setText("EROR: Enter the name")
                return
            else:
                self.ui.err.setText("")  
                self.cursorDB.execute('SELECT hour, min, sec FROM bd WHERE task = ?', (self.task_name_for_update_1,))
                self.results_new_1 = self.cursorDB.fetchall()
                for self.o in self.results_new_1:
                    self.new_h_1_1 = self.o[0]
                    self.new_min_1_1 = self.o[1]
                    self.new_sec_1_1 = self.o[2]

                self.parm3_1 = int(self.all_sec_1_1) + int(self.new_sec_1_1)

                if self.parm3_1 >= 60:
                    self.seconds_1 = self.parm3_1
                    self.seconds_1 = self.seconds_1 % (24 * 3600)
                    self.hour_1 = self.seconds_1 // 3600
                    self.seconds_1 %= 3600
                    self.minutes_1 = self.seconds_1 // 60
                    self.seconds_1 %= 60
                    self.other_time_1_1 = ("%d:%02d:%02d" % (self.hour_1, self.minutes_1, self.seconds_1))
                    self.xy_1 = self.other_time_1_1.split(':')

                    self.cursorDB.execute('UPDATE bd SET sec = ? WHERE task = ?', (self.xy_1[2], self.task_name_for_update_1))
                    self.cursorDB.execute('UPDATE bd SET min = ? WHERE task = ?', (int(self.new_min_1_1) + int(self.xy_1[1]), self.task_name_for_update_1))
                    self.cursorDB.execute('UPDATE bd SET hour = ? WHERE task = ?', (int(self.new_h_1_1) + int(self.xy_1[0]), self.task_name_for_update_1))
                    
                    self.cursorDB.execute('SELECT hour, min, sec FROM bd WHERE task = ?', (self.task_name_for_update_1,))
                else:
                    self.cursorDB.execute('UPDATE bd SET sec = ? WHERE task = ?', (self.parm3_1, self.task_name_for_update_1))

                self.cursorDB.execute('SELECT hour, min, sec FROM bd WHERE task = ?', (self.task_name_for_update_1,))
                self.results_new_1 = self.cursorDB.fetchall()
                for self.o in self.results_new_1:
                    self.new_min_1_1 = int(self.o[1])
                    
                self.parm2_1 = int(self.all_min_1_1) + int(self.new_min_1_1)

                if self.parm2_1 >= 60: 
                    self.min_1 = self.parm2_1
                    self.min_1 = self.min_1 % (24*3600)
                    self.Hour_1 = self.min_1 // 60
                    self.min_1 %= 60
                    self.other_time_1_1 = ("%d:%d" % (self.Hour_1, self.min_1))
                    self.xu_1 = self.other_time_1_1.split(':')

                    self.cursorDB.execute('UPDATE bd SET min = ? WHERE task = ?', (int(self.xu_1[1]), self.task_name_for_update_1))
                    self.cursorDB.execute('UPDATE bd SET hour = ? WHERE task = ?', (int(self.new_h_1_1) + int(self.xu_1[0]), self.task_name_for_update_1))
                else:
                    self.cursorDB.execute('UPDATE bd SET min = ? WHERE task = ?', (self.parm2_1, self.task_name_for_update_1))

                self.cursorDB.execute('SELECT hour, min, sec FROM bd WHERE task = ?', (self.task_name_for_update_1,))
                self.results_new_1 = self.cursorDB.fetchall()
                for self.o in self.results_new_1:
                    self.new_h_1_1 = int(self.o[0])
                self.parm1_1 = int(self.all_h_1_1) + int(self.new_h_1_1)       
                self.cursorDB.execute('UPDATE bd SET hour = ? WHERE task = ?', (self.parm1_1, self.task_name_for_update_1))
        else:
            pass
        ###Disconnect#
        self.con.commit()
        self.con.close()
    ###############################################################################
    ###delete btn###   
    def deleteTask(self):
        self.db_check()
        self.con = sl.connect('tasktime.db')
        self.cursor_2 = self.con.cursor()
        self.task_name_5 = self.ui.line_login.text()
        self.cursor_2.execute("DELETE FROM bd WHERE task=?", (self.task_name_5,))
        self.ui.info.setText("INFO: Task Delete")
        self.con.commit()
        self.con.close()
    ###############################################################################
    ###Timers for Task###
    def timersec(self):
        self.count = 0
        self.count_progress = 0
        self.flag = False
        self.ui.Time_1.setText(str(self.count))
        # add action to the method
        self.ui.start_btn_1.clicked.connect(self.starttime)
        self.ui.stop_btn_1.clicked.connect(self.stoptime)
        self.ui.pause_btn_1.clicked.connect(self.pausetime)
        self.timer2 = QTimer(self) 
        # adding action to timer
        self.connect(self.timer2, SIGNAL("timeout()"), self.showTime2)
        self.timer2.start(1000) #-Скорость таймера задачи
    def timersec_1(self):
        self.count_1 = 0
        self.count_progress_1 = 0
        self.flag_1 = False
        self.ui.Time_2.setText(str(self.count_1))
        # add action to the method
        self.ui.start_btn_2.clicked.connect(self.starttime_1)
        self.ui.stop_btn_2.clicked.connect(self.stoptime_1)
        self.ui.pause_btn_2.clicked.connect(self.pausetime_1)
        self.timer3 = QTimer(self) 
        # adding action to timer
        self.connect(self.timer3, SIGNAL("timeout()"), self.showTime3)
        self.timer3.start(1000)    #-Скорость таймера задачи

    def showTime2(self):
        # checking if flag is true
        if self.flag:
            # incrementing the counter
            self.count+= 1
            
        #converting
        self.output = (str(dt.timedelta(seconds=self.count)))
        # showing text
        self.ui.Time_1.setText(self.output)
        self.x = self.output.split(':')
        self.all_sec_1 = str(self.x[2])
        self.all_min_1 = str(self.x[1])
        self.all_h_1 = str(self.x[0])
        self.ui.label_10.setText(self.all_sec_1)
        self.ui.label_8.setText(self.all_min_1)
        self.ui.label_6.setText(self.all_h_1)
    def showTime3(self):
        # checking if flag is true
        if self.flag_1:
            # incrementing the counter
            self.count_1+= 1
            
        #converting
        self.output_1 = (str(dt.timedelta(seconds=self.count_1)))
        # showing text
        self.ui.Time_2.setText(self.output_1)
        self.x = self.output_1.split(':')
        self.all_sec_1_1 = str(self.x[2])
        self.all_min_1_1 = str(self.x[1])
        self.all_h_1_1 = str(self.x[0])
        self.ui.label_16.setText(self.all_sec_1_1)
        self.ui.label_14.setText(self.all_min_1_1)
        self.ui.label_12.setText(self.all_h_1_1)
    ###############################################################################
    ###Timers for update###
    def timer_save(self):
        self.count_update = 0
        self.timer_update = QTimer()
        self.connect(self.timer, SIGNAL("timeout()"), self.show_timer_update)
        self.timer_update.start(1000) #start timer with 1000ms (1 second) interval
    
    def show_timer_update (self):
        self.count_update+= 1
        self.output_update = (str(dt.timedelta(seconds=self.count_update)))
        self.y = self.output_update.split(':')
        self.out_sec_1 = str(self.y[2])
        if self.y[2] == '59':
            self.ui.info.setText("INFO: update BD")
            self.print_db_data()
            self.count_update = 0
            self.ui.err.setText("")
        elif self.y[2] == '10':
            self.ui.info.setText("INFO: save in BD")
        elif self.y[2] == '01' or self.y[2] == '05' or self.y[2] == '10' or self.y[2] == '15' or self.y[2] == '20' or self.y[2] == '25' or self.y[2] == '30' or self.y[2] == '35' or self.y[2] == '40' or self.y[2] == '45' or self.y[2] == '50' or self.y[2] == '55' :
            self.change()
        else:
            self.ui.info.setText("")
    ###############################################################################
    ###Open menu and pages###       
    def open_task_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
    def open_db_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
    def open_contact_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
    ##############################################################################
    ###Function Class __init###
    def __init__(self): #конструктор класса ExampleApp
        QMainWindow.__init__(self) # конструктор класса __init__ чтобы пользоватся атрибутами QMainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ##############################################################################
        ###Remove window title bar###
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ##############################################################################
        ###Set main background to transparent###
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ###############################################################################
        ###If left mouse button is clicked###
        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        ##############################################################################
        ###Resize window zone###
        # Создаем QSizeGrip для правого нижнего угла
        QSizeGrip(self.ui.resize_window)
        ##############################################################################
        ###check selected item###
        
        ##############################################################################
        ###Click event to move the window###
        self.ui.err.mouseMoveEvent = moveWindow
        self.ui.info.mouseMoveEvent = moveWindow
        self.ui.widget_40.mouseMoveEvent = moveWindow
        self.ui.widget_41.mouseMoveEvent = moveWindow
        self.ui.Clock.mouseMoveEvent = moveWindow
        ##############################################################################
        ###Minimize window###
        self.ui.roll_btn.clicked.connect(lambda: self.showMinimized())
        ##############################################################################
        ###Close window###
        self.ui.clouse_btn.clicked.connect(lambda: self.close())
        ##############################################################################
        ###Click btn start\stop\pause\accept\delete###
        self.ui.start_btn_1.clicked.connect(self.starttime)
        self.ui.accept_btn_1.clicked.connect(self.createTask)
        self.ui.delete_btn_1.clicked.connect(self.deleteTask)

        self.ui.pushButton_time.clicked.connect(self.open_task_page)
        self.ui.pushButton_db.clicked.connect(self.open_db_page)
        self.ui.pushButton_contact.clicked.connect(self.open_contact_page)
        #btn commit
        self.ui.add_line_btn.clicked.connect(self.commit_comment)
        ##############################################################################
        ###Telegramm and iphone###
        self.ui.telegram_btn.clicked.connect(self.url_telegram)
        ##############################################################################
        ###Clock###
        self.timer = QTimer()
        self.connect(self.timer, SIGNAL("timeout()"), self.showTime)
        self.timer.start(1000) #start timer with 1000ms (1 second) interval
        ##############################################################################
        ###Timer_save###
        self.timer_save()
        ##############################################################################
        ###Timer###
        self.timersec()
        self.timersec_1()
        ##############################################################################
        ###print all task in bd + time###
        self.print_db_data()
        ##############################################################################
        ###Show Window###
        self.show()  
    ###############################################################################
    ###Clock###
    def showTime(self):
        self.time = QTime.currentTime()
        self.txt_clock = self.time.toString('hh:mm')

        if (self.time.second() % 2) == 0:# эффект мигания двоеточия на часах
            self.txt_clock = self.txt_clock.replace(":", " ")

        self.ui.Clock.display(self.txt_clock)
    ##############################################################################
    ###Add mouse events to the window###
    def mousePressEvent (self, event):
        self.clickPosition = event.globalPos() #get current position of the mouse 
##############################################################################
###Execute app###
if __name__ == "__main__":
    app_main = QApplication(sys.argv) #создание потока для приложения
    window_main=MainWindow()
    sys.exit(app_main.exec_()) #завершение потока
