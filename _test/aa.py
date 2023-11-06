
import sys
import os
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QSizePolicy, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        label = QLabel('Main App', parent=self)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 600, 200
        self.setFixedSize(self.window_width, self.window_height)

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')
        labels['Username'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['Username'] = QLineEdit()
        self.lineEdits['Password'] = QLineEdit()
        self.lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels['Username'],            0, 0, 1, 1)
        layout.addWidget(self.lineEdits['Username'],    0, 1, 1, 3)

        layout.addWidget(labels['Password'],            1, 0, 1, 1)
        layout.addWidget(self.lineEdits['Password'],    1, 1, 1, 3)

        button_login = QPushButton('&Log In', clicked=self.checkCredential)
        layout.addWidget(button_login,                  2, 3, 1, 1)


    def checkCredential(self):
        username = self.lineEdits['Username'].text()
        password = self.lineEdits['Password'].text()

        if username == 'zalupa' and password == 'negra':
            time.sleep(1)
            self.mainApp = MainApp()
            self.mainApp.show()
            self.close()
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Loggin error!")
            dlg.setText("The username or password is incorrect")
            dlg.exec()


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 25px;
        }
        QLineEdit {
            height: 200px;
        }
    ''')
    
    loginWindow = LoginWindow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')