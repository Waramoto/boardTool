from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QLineEdit, QListWidget
from PyQt5.QtCore import Qt
import sys, os, psycopg2, subprocess, shutil
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
        if self.lang == '1':
            self.path = 'ui/UA/'
        elif self.lang == '2':
            self.path = 'ui/RU/'
        else:
            self.path = 'ui/EN/'
        self.login = uic.loadUi(self.path + 'login.ui', self)
        self.login.buttonExit = self.findChild(QPushButton, 'ExitButton')
        self.login.buttonExit.clicked.connect(self.offScript)
        self.login.buttonLogin = self.findChild(QPushButton, 'LoginButton')
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
        self.login.LoginEdit = self.findChild(QLineEdit, 'LoginEdit')
        self.login.PassEdit = self.findChild(QLineEdit, 'PassEdit')
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
        self.main = uic.loadUi(self.path + 'mainwindow.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.main.buttonOff = self.findChild(QPushButton, 'OffButton')
        self.main.buttonOff.clicked.connect(self.offScript)
        self.main.buttonSettings = self.findChild(QPushButton, 'SettingsButton')
        self.main.buttonSettings.clicked.connect(self.SettingsApp)
        self.main.buttonLabs = self.findChild(QPushButton, 'LabsButton')
        self.main.buttonLabs.clicked.connect(self.LabsApp)
        self.main.buttonDump = self.findChild(QPushButton, 'DumpButton')
        self.showFullScreen()
        self.f.close()

    def offScript(self):
        self.f = open('ui/language.txt', 'r')
        self.lang = self.f.read()
        if self.lang == '1':
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Увага")
            msgBox.setText("Ви впевнені?")
            self.buttonYes = msgBox.addButton("Так", QMessageBox.YesRole)
            self.buttonNo = msgBox.addButton("Ні", QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == self.buttonYes:
                os.chmod("./scripts/shutdown.sh", 0o755)
                os.system("./scripts/shutdown.sh")
        elif self.lang == '2':
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Внимание")
            msgBox.setText("Вы уверены?")
            self.buttonYes = msgBox.addButton("Да", QMessageBox.YesRole)
            self.buttonNo = msgBox.addButton("Нет", QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == self.buttonYes:
                os.chmod("./scripts/shutdown.sh", 0o755)
                os.system("./scripts/shutdown.sh")
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Attention")
            msgBox.setText("Are you sure?")
            self.buttonYes = msgBox.addButton("Yes", QMessageBox.YesRole)
            self.buttonNo = msgBox.addButton("No", QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == self.buttonYes:
                os.chmod("./scripts/shutdown.sh", 0o755)
                os.system("./scripts/shutdown.sh")
        self.f.close()

    def labOpenScript(self):
        if len(self.labs.listLabs.selectedItems()) == 0:
            self.f = open('ui/language.txt', 'r')
            self.lang = self.f.read()
            if self.lang == '1':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle("Помилка")
                msgBox.setText("Оберіть файл")
                msgBox.exec_()
            elif self.lang == '2':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Выберите файл")
                msgBox.exec_()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Select a file")
                msgBox.exec_()
            self.f.close()
        else:
            self.labname = self.labs.listLabs.selectedItems()[0].text()
            os.system('scripts/labs/' + self.labname)

    def labAddScript(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName(filter = "Scripts (*.sh)")
        if not self.file:
            self.filename = os.path.basename(self.file[0])
            self.filelist = os.listdir('scripts/labs/')
            if self.filename in self.filelist:
                self.f = open('ui/language.txt', 'r')
                self.lang = self.f.read()
                if self.lang == '1':
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Question)
                    msgBox.setWindowTitle("Увага")
                    msgBox.setText("Файл з таким ім'ям вже існує. Замінити?")
                    self.buttonYes = msgBox.addButton("Так", QMessageBox.YesRole)
                    self.buttonNo = msgBox.addButton("Ні", QMessageBox.NoRole)
                    msgBox.exec_()
                    if msgBox.clickedButton() == self.buttonYes:
                        shutil.copy(self.file[0], 'scripts/labs/')
                        self.labs.listLabs.addItem(self.filename)
                elif self.lang == '2':
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Question)
                    msgBox.setWindowTitle("Внимание")
                    msgBox.setText("Файл с таким именем уже существует. Заменить?")
                    self.buttonYes = msgBox.addButton("Да", QMessageBox.YesRole)
                    self.buttonNo = msgBox.addButton("Нет", QMessageBox.NoRole)
                    msgBox.exec_()
                    if msgBox.clickedButton() == self.buttonYes:
                        shutil.copy(self.file[0], 'scripts/labs/')
                        self.labs.listLabs.addItem(self.filename)
                else:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Question)
                    msgBox.setWindowTitle("Attention")
                    msgBox.setText("A file with the same name already exists. Replace?")
                    self.buttonYes = msgBox.addButton("Yes", QMessageBox.YesRole)
                    self.buttonNo = msgBox.addButton("No", QMessageBox.NoRole)
                    msgBox.exec_()
                    if msgBox.clickedButton() == self.buttonYes:
                        shutil.copy(self.file[0], 'scripts/labs/')
                        self.labs.listLabs.addItem(self.filename)
                self.f.close()
            else:
                shutil.copy(self.file[0], 'scripts/labs/')
                self.labs.listLabs.addItem(self.filename)

    def labDeleteScript(self):
        if len(self.labs.listLabs.selectedItems()) == 0:
            self.f = open('ui/language.txt', 'r')
            self.lang = self.f.read()
            if self.lang == '1':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle("Помилка")
                msgBox.setText("Оберіть файл")
                msgBox.exec_()
            elif self.lang == '2':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Выберите файл")
                msgBox.exec_()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Select a file")
                msgBox.exec_()
            self.f.close()
        else:
            self.filename = self.labs.listLabs.selectedItems()[0].text()
            self.labname = self.labs.listLabs.selectedItems()[0]
            self.f = open('ui/language.txt', 'r')
            self.lang = self.f.read()
            if self.lang == '1':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setWindowTitle("Увага")
                msgBox.setText("Ви впевнені?")
                self.buttonYes = msgBox.addButton("Так", QMessageBox.YesRole)
                self.buttonNo = msgBox.addButton("Ні", QMessageBox.NoRole)
                msgBox.exec_()
                if msgBox.clickedButton() == self.buttonYes:
                    os.remove('scripts/labs/' + self.filename)
                    for lab in self.labs.listLabs.selectedItems():
                        self.labs.listLabs.takeItem(self.labs.listLabs.row(lab))
            elif self.lang == '2':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setWindowTitle("Внимание")
                msgBox.setText("Вы уверены?")
                self.buttonYes = msgBox.addButton("Да", QMessageBox.YesRole)
                self.buttonNo = msgBox.addButton("Нет", QMessageBox.NoRole)
                msgBox.exec_()
                if msgBox.clickedButton() == self.buttonYes:
                    os.remove('scripts/labs/' + self.filename)
                    for lab in self.labs.listLabs.selectedItems():
                        self.labs.listLabs.takeItem(self.labs.listLabs.row(lab))
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setWindowTitle("Attention")
                msgBox.setText("Are you sure?")
                self.buttonYes = msgBox.addButton("Yes", QMessageBox.YesRole)
                self.buttonNo = msgBox.addButton("No", QMessageBox.NoRole)
                msgBox.exec_()
                if msgBox.clickedButton() == self.buttonYes:
                    os.remove('scripts/labs/' + self.filename)
                    for lab in self.labs.listLabs.selectedItems():
                        self.labs.listLabs.takeItem(self.labs.listLabs.row(lab))
            self.f.close()

    def LabsApp(self):
        self.main.close()
        super(Ui, self).__init__()
        self.labs = uic.loadUi(self.path + 'labs.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.filelist = os.listdir('scripts/labs/')
        self.labs.listLabs = self.findChild(QListWidget, 'LabsList')
        self.labs.listLabs.addItems(self.filelist)
        self.labs.buttonOpen = self.findChild(QPushButton, 'OpenButton')
        self.labs.buttonOpen.clicked.connect(self.labOpenScript)
        self.labs.buttonAdd = self.findChild(QPushButton, 'AddButton')
        self.labs.buttonAdd.clicked.connect(self.labAddScript)
        self.labs.buttonDelete = self.findChild(QPushButton, 'DeleteButton')
        self.labs.buttonDelete.clicked.connect(self.labDeleteScript)
        self.labs.buttonBack2 = self.findChild(QPushButton, 'Back2Button')
        self.labs.buttonBack2.clicked.connect(self.MainApp)
        self.showFullScreen()
        self.f.close()

    def SettingsApp(self):
        self.main.close()
        super(Ui, self).__init__()
        self.settings = uic.loadUi(self.path + 'settings.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.settings.buttonLanguage = self.findChild(QPushButton, 'LanguageButton')
        self.settings.buttonLanguage.clicked.connect(self.LanguageApp)
        self.settings.buttonBack0 = self.findChild(QPushButton, 'Back0Button')
        self.settings.buttonBack0.clicked.connect(self.MainApp)
        self.showFullScreen()
        self.f.close()

    def LanguageApp(self):
        self.settings.close()
        super(Ui, self).__init__()
        self.language = uic.loadUi(self.path + 'language.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.language.buttonEN = self.findChild(QPushButton, 'ENButton')
        self.language.buttonEN.clicked.connect(self.EN)
        self.language.buttonEN.clicked.connect(self.SettingsApp)
        self.language.buttonUA = self.findChild(QPushButton, 'UAButton')
        self.language.buttonUA.clicked.connect(self.UA)
        self.language.buttonUA.clicked.connect(self.SettingsApp)
        self.language.buttonRU = self.findChild(QPushButton, 'RUButton')
        self.language.buttonRU.clicked.connect(self.RU)
        self.language.buttonRU.clicked.connect(self.SettingsApp)
        self.language.buttonBack1 = self.findChild(QPushButton, 'Back1Button')
        self.language.buttonBack1.clicked.connect(self.SettingsApp)
        self.showFullScreen()
        self.f.close()

    def EN(self):
        self.path = 'ui/EN/'
        self.f = open('ui/language.txt', 'w')
        self.f.write("0")
        self.f.close()

    def UA(self):
        self.path = 'ui/UA/'
        self.f = open('ui/language.txt', 'w')
        self.f.write("1")
        self.f.close()

    def RU(self):
        self.path = 'ui/RU/'
        self.f = open('ui/language.txt', 'w')
        self.f.write("2")
        self.f.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.showFullScreen()
app.exec_()
