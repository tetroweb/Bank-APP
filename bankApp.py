from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json


css = """
    QLineEdit{border:none;}
    QLineEdit::focus{border-bottom: 1px solid green}
    """

class users():
    def __init__(self,name,id,password,gender,money):
        self.name = name
        self.id = id
        self.password = password
        self.gender = gender
        self.money = money
    try:
        def save_user(self):
            users = "users.txt"
            with open(users, "a") as dosya:
                dosya.write(f"Name : {self.name}, ID: {self.id}, Sifre: {self.password}, Cinsiyet: {self.gender}, Maas :{self.money}\n")
    except Exception as hata:
        print("Bir hata oluştu:", hata)

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.vbox = QVBoxLayout(self)
        
        self.hbox1 = QHBoxLayout()
        self.form1 = QFormLayout()
        
        self.vbox.addLayout(self.form1)
        
        
        self.id_label = QLabel("ID / CUSTOMER ID :")
        self.id_label.setFont(QFont("Tahoma",10))
        self.id_label.setContentsMargins(140,0,0,0)
        
        self.id_edit = QLineEdit()
        self.id_edit.setFixedWidth(150)
        self.id_edit.setFont(QFont("Tahoma",12))
        self.id_edit.setStyleSheet(css)
        self.id_edit.setContentsMargins(0,0,0,0)
        self.id_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.id_edit.setMaxLength(11)
        
        
        self.form1.addRow(self.id_label,self.id_edit)
        
        self.password_label = QLabel("Password :")
        self.password_label.setContentsMargins(140,0,0,0)
        self.password_label.setFont(QFont("Tahoma",10))
        
        
        self.password_edit = QLineEdit()
        self.password_edit.setFixedWidth(150)
        self.password_edit.setFont(QFont("Tahoma",12))
        self.password_edit.setStyleSheet(css)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setMaxLength(6)
        self.password_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        
        self.show_button = QPushButton()
        self.show_button.setIcon(QIcon("hide_pass.png"))
        self.show_button.setFixedWidth(50)
        self.show_button.clicked.connect(self.show_password)
        self.show_button.setStyleSheet("""
            QPushButton {
                background-color: #018000;
                color: white;
                border: none;
                padding:2px;
                border-radius: 3px;
            }
            
            QPushButton:hover {
                background-color: #5EBF00;
                
            }
        """)
        
        
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.password_edit)
        self.hbox2.addWidget(self.show_button)
        
        self.form1.addRow(self.password_label,self.hbox2)
        self.form1.setContentsMargins(0,250,80,0)
        
        
        self.login_button = QPushButton("Login")
        self.login_button.setFixedWidth(70)
        self.login_button.clicked.connect(self.open_Main_Window)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #018000;
                color: white;
                border: none;
                padding:2px;
                border-radius: 3px;
            }
            
            QPushButton:hover {
                background-color: #5EBF00;
                
            }
        """)
        
        self.forgot_password = QLabel("forgot password")
        self.forgot_password.setFont(QFont("Tahoma",6))
        self.forgot_password.setStyleSheet("color:#888897")
        self.forgot_password.mousePressEvent = self.forgot_password_clicked
        
                
        self.hbox_login = QHBoxLayout()
        self.hbox_login.addWidget(self.login_button)
        self.hbox_login.addWidget(self.forgot_password)
        self.hbox_login.setAlignment(Qt.AlignHCenter)
        
        self.form1.addRow(self.hbox_login)
        
        
        self.hbox_sign = QHBoxLayout()
        self.sign_button = QPushButton("Sign Up")
        self.sign_button.setFixedWidth(80)
        self.sign_button.clicked.connect(self.show_sign_window)
        self.sign_button.setStyleSheet("""
            QPushButton{
                background-color: #018000;
                color: white;
                border: none;
                padding:2px;
                border-radius: 3px;
            }
             QPushButton:hover {
                background-color: #5EBF00;
            }    
        """)
        self.hbox_sign.addWidget(self.sign_button)
        self.hbox_sign.setAlignment(Qt.AlignHCenter)
        self.form1.addRow(self.hbox_sign)
        
        self.setFixedSize(650,700)
        self.show()
    
    
    def show_password(self,e):
        if self.password_edit.echoMode() == QLineEdit.Normal:
            self.password_edit.setEchoMode(QLineEdit.Password)
            self.show_button.setIcon(QIcon("hide_pass.png"))
        else:
            self.password_edit.setEchoMode(QLineEdit.Normal)
            self.show_button.setIcon(QIcon("show_pass.png"))
    
    def show_sign_window(self,e):
        self.sign_window = SignUpWindow()
        self.sign_window.show()
    
    def open_Main_Window(self,e):
        with open('users.json', 'r') as dosya:
            users = json.load(dosya)
        try:
        
            if users[self.id_edit.text()] == self.password_edit.text() :
                    self.Main_Window = Main_Window()
                    self.Main_Window.show()
            
            if self.password_edit.text()  in users:
                    self.Main_Window = Main_Window()
                    self.Main_Window.show()  
            
        except KeyError :
            if self.id_edit.text() !="" :
                self.id_edit.clear()
                self.id_edit.setPlaceholderText("ID is wrong")
        if self.password_edit.text() not in users and self.password_edit.text() !="":
                    self.password_edit.clear()
                    self.password_edit.setPlaceholderText("password is wrong")  
        
    def forgot_password_clicked(self,e):
        
        self.show_window = New_Password_Window()
        self.show_window.show()

class New_Password_Window(QWidget):
        
    def __init__(self):
        super().__init__()
        
        
        self.vbox = QVBoxLayout(self)
        self.form = QFormLayout()
        self.vbox.addLayout(self.form)
        self.form.setContentsMargins(0,160,0,0)
        
        
        self.first_row = QHBoxLayout()
        self.second_row = QHBoxLayout()
        self.third_row = QHBoxLayout()
        
        self.old_password_label = QLabel("Eski Şifre :")
        self.old_password_label.setFont(QFont("Tahoma",10))
        self.old_password_edit = QLineEdit()
        self.old_password_edit.setFont(QFont("Tahoma",12))
        self.old_password_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.old_password_edit.setFixedWidth(150)
        self.first_row.setAlignment(Qt.AlignHCenter)
        
        self.new_password_label = QLabel("Yeni Şifre :")
        self.new_password_label.setFont(QFont("Tahoma",10))
        self.new_password_edit = QLineEdit()
        self.new_password_edit.setFont(QFont("Tahoma",12))
        self.new_password_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.new_password_edit.setFixedWidth(150)
        
        self.first_row.addWidget(self.old_password_label)
        self.first_row.addWidget(self.old_password_edit)
        self.first_row.setContentsMargins(20,0,0,0)
        
        self.second_row.addWidget(self.new_password_label)
        self.second_row.addWidget(self.new_password_edit)
        self.second_row.setContentsMargins(20,0,0,0)
        
        self.form.addRow(self.first_row)
        self.form.addRow(self.second_row)
        self.form.addRow(self.third_row)
        
        self.save_button = QPushButton("Save")
        self.save_button.setFixedWidth(80)
        self.third_row.setContentsMargins(140,0,0,0)
        self.save_button.clicked.connect(self.save_password)
        
        
        
        
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #018000;
                color: white;
                border: none;
                padding:2px;
                border-radius: 3px;
            }
            
            QPushButton:hover {
                background-color: #5EBF00;
                
            }
        """)
        
        self.third_row.addWidget(self.save_button)
        self.form.addRow(self.third_row)
        
        
        self.setWindowTitle("Reset Password")
        self.resize(300,400)

    def save_password(self,e):
        with open('users.json', 'r') as dosya:
            self.users = json.load(dosya)
        self.keys = list(self.users.keys()) 
        
        if self.old_password_edit.text() in self.users.values():
            for value in self.keys: 
                self.users[value] = self.new_password_edit.text()
                with open('users.json', 'w') as dosya:
                    json.dump(self.users, dosya)
                self.save_button.close()
                self.succes_label = QLabel("şifre sifirlandi")
                self.succes_label.setStyleSheet("color: green;")
                self.third_row.addWidget(self.succes_label)
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.close)
                self.timer.start(1000)   
    
class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UserSign = UserSign()
        
        self.setWindowTitle('Sign Window')
        
        self.vbox = QVBoxLayout(self)
        self.form = QFormLayout()
        self.vbox.addLayout(self.form)
        self.form.setContentsMargins(0,160,0,0)
        
        
        self.first_row = QHBoxLayout()
        self.second_row = QHBoxLayout()
        self.third_row = QHBoxLayout()
        self.fourth_row = QHBoxLayout()
        
        
        self.username_label = QLabel("ID :")
        self.username_label.setFont(QFont("Tahoma",10))
        self.username_edit = QLineEdit()
        self.username_edit.setFont(QFont("Tahoma",12))
        self.username_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.username_edit.setFixedWidth(150)
        self.first_row.setAlignment(Qt.AlignHCenter)
        
        self.password_label = QLabel("Password :")
        self.password_label.setFont(QFont("Tahoma",10))
        self.password_edit = QLineEdit()
        self.password_edit.setFont(QFont("Tahoma",12))
        self.password_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.password_edit.setFixedWidth(150)
        
       
        
        
        self.save_button = QPushButton("Save")
        self.save_button.setFixedWidth(80)
        self.third_row.setContentsMargins(140,0,0,0)
        self.save_button.clicked.connect(self.sign_users)
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #018000;
                color: white;
                border: none;
                padding:2px;
                border-radius: 3px;
            }
            
            QPushButton:hover {
                background-color: #5EBF00;
                
            }
        """)
        
        self.first_row.addWidget(self.username_label)
        self.first_row.addWidget(self.username_edit)
        self.first_row.setContentsMargins(60,0,50,0)
        
        self.second_row.addWidget(self.password_label)
        self.second_row.addWidget(self.password_edit)
        self.second_row.setContentsMargins(60,0,50,0)
        
        self.gender_label = QLabel("Cinsiyet :")
        self.gender_radio_male = QRadioButton("Erkek")
        self.gender_radio_female = QRadioButton("Kadin")
        
        self.third_row.addWidget(self.gender_radio_male)
        self.third_row.addWidget(self.gender_radio_female)
        
        self.form.addRow(self.gender_label,self.third_row)
        
        
        
        self.fourth_row.addWidget(self.save_button)
        
        self.form.addRow(self.first_row)
        self.form.addRow(self.second_row)
        self.form.addRow(self.third_row)
        
        
        self.resize(300,500)
        
    def sign_users(self,e):
        self.UserSign.add_user(self.username_edit.text(),self.password_edit.text())
        self.close()

class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(500,500)       

class UserSign:
    def __init__(self):
        self.users = {}  

    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}
    
    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file)
    
    def add_user(self, username, password):
        if username not in self.users:
            self.users[username] = password
            self.save_users()
        

user1 = users("Berkant","11347318604","1345790","Male","45000")  
user1.save_user()     
app = QApplication([])
window = main()
app.exec()