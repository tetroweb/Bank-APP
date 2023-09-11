from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json


css = """
    QLineEdit{border:none;}
    QLineEdit::focus{border-bottom: 1px solid green}
    """

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
        
        self.third_row.addWidget(self.save_button)
        
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
    
    
class main(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.vbox = QVBoxLayout(self)
        
        self.hbox1 = QHBoxLayout()
        self.form1 = QFormLayout()
        
        self.vbox.addLayout(self.form1)
        
        
        self.label1 = QLabel("ID / CUSTOMER ID :")
        self.label1.setFont(QFont("Tahoma",10))
        self.label1.setContentsMargins(140,0,0,0)
        
        self.edit1 = QLineEdit()
        self.edit1.setFixedWidth(150)
        self.edit1.setFont(QFont("Tahoma",12))
        self.edit1.setStyleSheet(css)
        self.edit1.setContentsMargins(0,0,0,0)
        self.edit1.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.edit1.setMaxLength(11)
        
        self.form1.addRow(self.label1,self.edit1)
        
        self.label2 = QLabel("Password :")
        self.label2.setContentsMargins(140,0,0,0)
        self.label2.setFont(QFont("Tahoma",10))
        
        
        self.edit2 = QLineEdit()
        self.edit2.setFixedWidth(150)
        self.edit2.setFont(QFont("Tahoma",12))
        self.edit2.setStyleSheet(css)
        self.edit2.setEchoMode(QLineEdit.Password)
        self.edit2.setMaxLength(6)
        self.edit2.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        
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
        self.hbox2.addWidget(self.edit2)
        self.hbox2.addWidget(self.show_button)
        
        self.form1.addRow(self.label2,self.hbox2)
        self.form1.setContentsMargins(0,250,80,0)
        
        
        self.login_button = QPushButton("Login")
        self.login_button.setFixedWidth(70)
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
        self.login_button.clicked.connect(self.open_Main_Window)
                
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
        if self.edit2.echoMode() == QLineEdit.Normal:
            self.edit2.setEchoMode(QLineEdit.Password)
            self.show_button.setIcon(QIcon("hide_pass.png"))
        else:
            self.edit2.setEchoMode(QLineEdit.Normal)
            self.show_button.setIcon(QIcon("show_pass.png"))
    
    def show_sign_window(self,e):
        self.sign_window = SignUpWindow()
        self.sign_window.show()
    
    def open_Main_Window(self,e):
        with open('users.json', 'r') as dosya:
            users = json.load(dosya)
        
        if users[self.edit1.text()] == self.edit2.text():
            self.Main_Window = Main_Window()
            self.Main_Window.show()
    
         
app = QApplication([])
window = main()
app.exec()