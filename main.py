from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt
import sys, os, psycopg2, subprocess
from base.config import config

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.background = uic.loadUi('ui/background.ui', self)
        self.showFullScreen()

        super(Ui, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.f = open('ui/language.txt', 'r')
        self.lang = self.f.read()
        if (self.lang == '1'):
            self.login = uic.loadUi('ui/UA_login.ui', self)
        elif (self.lang == '2'):
            self.login = uic.loadUi('ui/RU_login.ui', self)
        else:
            self.login = uic.loadUi('ui/EN_login.ui', self)
        self.login.buttonExit = self.findChild(QtWidgets.QPushButton, 'ExitButton')
        self.login.buttonExit.clicked.connect(self.close)
        self.login.buttonLogin = self.findChild(QtWidgets.QPushButton, 'LoginButton')
        self.login.buttonLogin.clicked.connect(self.LoginApp)
        self.showFullScreen()
        self.f.close()

    def checkConnect(self):
        params = config()
        try:
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.close()
            conn.close()
        except:
            self.DefLogin = "admin"
            self.DefPass = "admin"

    def LoginApp(self):
        self.login.LoginEdit = self.findChild(QtWidgets.QLineEdit, 'LoginEdit')
        self.login.PassEdit = self.findChild(QtWidgets.QLineEdit, 'PassEdit')
        loginVvod = str(self.login.LoginEdit.text())
        passVvod = str(self.login.PassEdit.text())
        self.checkConnect()

        if loginVvod == self.DefLogin:
            if passVvod == self.DefPass:
                self.MainApp()
            else:
                print("No valid Data")
        else:
            print("No valid Data")

        print(loginVvod, passVvod)

    def MainApp(self):
        self.login.close()
        super(Ui, self).__init__()
        self.f = open('ui/language.txt', 'r')
        self.lang = self.f.read()
        if (self.lang == '1'):
            self.main = uic.loadUi('ui/UA_mainwindow.ui', self)
        elif (self.lang == '2'):
            self.main = uic.loadUi('ui/RU_mainwindow.ui', self)
        else:
            self.main = uic.loadUi('ui/EN_mainwindow.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.main.buttonOff = self.findChild(QtWidgets.QPushButton, 'OffButton')
        self.main.buttonOff.clicked.connect(self.offYesNo)
        self.main.buttonSettings = self.findChild(QtWidgets.QPushButton, 'SettingsButton')
        self.main.buttonSettings.clicked.connect(self.SettingsApp)
        self.main.buttonLabs = self.findChild(QtWidgets.QPushButton, 'LabsButton')
        self.main.buttonDump = self.findChild(QtWidgets.QPushButton, 'DumpButton')
        self.showFullScreen()
        self.f.close()

    def offYesNo(self):
        self.main.close()
        super(Ui, self).__init__()
        self.f = open('ui/language.txt', 'r')
        self.lang = self.f.read()
        if (self.lang == '1'):
            self.accept = uic.loadUi('ui/UA_accept.ui', self)
        elif (self.lang == '2'):
            self.accept = uic.loadUi('ui/RU_accept.ui', self)
        else:
            self.accept = uic.loadUi('ui/EN_accept.ui', self)
        self.accept.buttonYes = self.findChild(QtWidgets.QPushButton, 'YesButton')
        self.accept.buttonYes.clicked.connect(self.offScript)
        self.accept.buttonNo = self.findChild(QtWidgets.QPushButton, 'NoButton')
        self.accept.buttonNo.clicked.connect(self.MainApp)
        self.showFullScreen()
        self.f.close()

    def offScript(self):
        os.chmod("./scripts/shutdown.sh", 0o755)
        os.system("./scripts/shutdown.sh")

    def SettingsApp(self):
        self.main.close()
        super(Ui, self).__init__()
        self.f = open('ui/language.txt', 'r')
        self.lang = self.f.read()
        if (self.lang == '1'):
            self.settings = uic.loadUi('ui/UA_settings.ui', self)
        elif (self.lang == '2'):
            self.settings = uic.loadUi('ui/RU_settings.ui', self)
        else:
            self.settings = uic.loadUi('ui/EN_settings.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.settings.buttonLanguage = self.findChild(QtWidgets.QPushButton, 'LanguageButton')
        self.settings.buttonLanguage.clicked.connect(self.LanguageApp)
        self.settings.buttonBackup = self.findChild(QtWidgets.QPushButton, 'BackupButton')
        self.settings.buttonBack0 = self.findChild(QtWidgets.QPushButton, 'Back0Button')
        self.settings.buttonBack0.clicked.connect(self.MainApp)
        self.showFullScreen()
        self.f.close()

    def LanguageApp(self):
        self.settings.close()
        super(Ui, self).__init__()
        self.f = open('ui/language.txt', 'r')
        self.lang = self.f.read()
        if (self.lang == '1'):
            self.language = uic.loadUi('ui/UA_language.ui', self)
        elif (self.lang == '2'):
            self.language = uic.loadUi('ui/RU_language.ui', self)
        else:
            self.language = uic.loadUi('ui/EN_language.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.language.buttonEN = self.findChild(QtWidgets.QPushButton, 'ENButton')
        self.settings.buttonEN.clicked.connect(self.EN)
        self.settings.buttonEN.clicked.connect(self.SettingsApp)
        self.language.buttonUA = self.findChild(QtWidgets.QPushButton, 'UAButton')
        self.settings.buttonUA.clicked.connect(self.UA)
        self.settings.buttonUA.clicked.connect(self.SettingsApp)
        self.language.buttonRU = self.findChild(QtWidgets.QPushButton, 'RUButton')
        self.settings.buttonRU.clicked.connect(self.RU)
        self.settings.buttonRU.clicked.connect(self.SettingsApp)
        self.language.buttonBack1 = self.findChild(QtWidgets.QPushButton, 'Back1Button')
        self.settings.buttonBack1.clicked.connect(self.SettingsApp)
        self.showFullScreen()
        self.f.close()

    def EN(self):
        self.f = open('ui/language.txt', 'w')
        self.f.write("0")
        self.f.close()

    def UA(self):
        self.f = open('ui/language.txt', 'w')
        self.f.write("1")
        self.f.close()

    def RU(self):
        self.f = open('ui/language.txt', 'w')
        self.f.write("2")
        self.f.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.showFullScreen()
app.exec_()
