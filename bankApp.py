from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

css = """
    QLineEdit{border:none;}
    QLineEdit::focus{border-bottom: 1px solid green}
    """
class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sign Window')
        
        self.vbox = QVBoxLayout(self)
        self.form = QFormLayout()
        self.vbox.addLayout(self.form)
        
        self.first_row = QHBoxLayout()
        
        self.username_label = QLabel("Username :")
        self.username_edit = QLineEdit()
         
        self.form.addWidget(self.username_label)
        self.form.addWidget(self.username_edit)
        
        self.form.addRow(self.first_row)
        
        self.resize(300,500)
        

class UserSign:
    def __init__(self):
        self.users = {}  

    def kullanici_ekle(self, username, password):
        if username not in self.users:
            self.users[username] = password


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.vbox = QVBoxLayout(self)
        
        self.hbox1 = QHBoxLayout()
        
        
        self.form1 = QFormLayout()
        
        
        self.vbox.addLayout(self.form1)
        
        
        self.label1 = QLabel("Username :")
        self.label1.setFont(QFont("Tahoma",10))
        self.label1.setContentsMargins(140,0,0,0)
        
        self.edit1 = QLineEdit()
        self.edit1.setFixedWidth(150)
        self.edit1.setFont(QFont("Tahoma",12))
        self.edit1.setStyleSheet(css)
        self.edit1.setContentsMargins(0,0,0,0)
        self.edit1.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        
        
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
        
        self.resize(500,700)
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
          
app = QApplication([])
window = main()
app.exec()