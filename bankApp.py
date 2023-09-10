from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

css = """
    QLineEdit{border:none;}
    QLineEdit::focus{border-bottom: 1px solid green}
    """
    


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.vbox = QVBoxLayout(self)
        
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        
        self.form1 = QFormLayout()
        self.form2 = QFormLayout()
        
        self.vbox.addLayout(self.form1)
        
        
         
         
        self.label1 = QLabel("Username :")
        self.label1.setFont(QFont("Tahoma",10))
        self.label1.setContentsMargins(140,0,0,0)
        
        self.edit1 = QLineEdit()
        self.edit1.setFixedWidth(150)
        self.edit1.setFont(QFont("Tahoma",12))
        self.edit1.setStyleSheet(css)
        self.edit1.setContentsMargins(0,0,0,0)
        
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
        
        self.show_button = QPushButton()
        self.show_button.setIcon(QIcon("hide_pass.png"))
        self.show_button.setFixedWidth(50)
        self.show_button.clicked.connect(self.show_password)
        
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.edit2)
        self.hbox2.addWidget(self.show_button)
        
        self.form1.addRow(self.label2,self.hbox2)
        self.form1.setContentsMargins(0,250,80,0)
        
        self.login_button = QPushButton("Login")
        self.login_button.setFixedWidth(70)
        self.setStyleSheet("""
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
        
        self.resize(500,700)
        self.show()
    
    
    def show_password(self,e):
        if self.edit2.echoMode() == QLineEdit.Normal:
            self.edit2.setEchoMode(QLineEdit.Password)
            self.show_button.setIcon(QIcon("hide_pass.png"))
        else:
            self.edit2.setEchoMode(QLineEdit.Normal)
            self.show_button.setIcon(QIcon("show_pass.png"))
        
app = QApplication([])
window = main()
app.exec()