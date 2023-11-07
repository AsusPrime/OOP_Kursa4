# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
                               QMessageBox, QTableWidgetItem, QHeaderView, QPushButton)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow, Ui_AddWindow, Ui_RemoveWindow
import pymysql

#AUXILIARY WINDOWS
#ADD WINDOW
class AddWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.addButton)

    def addButton(self):
        pass

#REMOVE WINDOW
class RemoveWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RemoveWindow()
        self.ui.setupUi(self)

#CHANGE WINDOW
class ChangeWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self)

#MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        #AUXILIARY VARIABLES
        self.anotherWin = None

        #WINDOW SETTINGS
        self.setFixedSize(800, 600)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #UPDATE DATA FROM DB
        self.ui.updateDBButton.clicked.connect(self.updateDB)

        #WINDOW BUTTONS
        self.ui.addButton.clicked.connect(self.add)
        self.ui.removeButton.clicked.connect(self.remove)
        self.ui.changeButton.clicked.connect(self.change)

        #ACTION BUTTONS
        self.ui.actionLog_out.triggered.connect(self.log_out)

        #DB
        self.db = DataBase()

    #BUTTONS ACTIVES
    def log_out(self):
        print('bye')

    def updateDB(self):
        data = self.db.getData()
        
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))

        column_names = ['ID', 'Name', 'Email', 'Password']
        self.ui.tableWidget.setHorizontalHeaderLabels(column_names)#Задаем имена столбцам
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)#Растягиваем столбцы по размеру содержимого

        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.ui.tableWidget.setItem(row_num, col_num, item)

    #WINDOWS
    def add(self):
        self.anotherWin = AddWindow()
        self.anotherWin.show()

    def remove(self):
        self.anotherWin = RemoveWindow()
        self.anotherWin.show()

    def change(self):
        self.anotherWin = ChangeWindow()
        self.anotherWin.show()

    #CLOSE EVENT
    def closeEvent(self, event):
        if self.anotherWin is not None:
            self.anotherWin.close()
        event.accept()


#DATA BASE CLASS
class DataBase:
    def __init__(self):
        try:#TRY TO CONNECT
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                password="Supy1011",
                database="shema")
            self.cursor = self.db.cursor()
        except Exception as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Connection error!")
            dlg.setText("Check your internet connection!")
            dlg.exec()
            sys.exit(-1)

    def getData(self):#RETURN DATA FROM DB
        try:
            self.cursor.execute("SELECT * FROM users;")
            data = self.cursor.fetchall()
            #result = "\n".join([str(row) for row in data])
            return data
        except Exception as ex:
            print(f'Error:\n{ex}')
            return -1

    def removeData(self, ID):
        pass

    def changeData(self, ID, changes):
        '''
        ID must containe id of the object that we want to change
        changes must have hash-map that have (atribute_name : new_atribute_value)
        '''
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
