from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3

connect = sqlite3.connect("customers.db")

css = """
    QLineEdit{border:none;}
    QLineEdit::focus{border-bottom: 1px solid green}
    """
    
class SignUpWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        print(self.size())
        self.background_label = QLabel(self)
        self.pixmap = QPixmap('sign_background.jpg')  # Resmin dosya yolu
        self.background_label.setPixmap(self.pixmap)
        self.background_label.setGeometry(0, -10,480,640)
        self.background_label.setStyleSheet("background-image: url('sign_background.jpg');")
        
        
        
        self.setWindowTitle('Sign Window')
        
        self.vbox = QVBoxLayout(self)
        self.form = QFormLayout()
        self.vbox.addLayout(self.form)
        self.form.setContentsMargins(0,150,0,0)
        
        
        self.first_row = QHBoxLayout()
        self.second_row = QHBoxLayout()
        self.third_row = QHBoxLayout()
        self.fourth_row = QHBoxLayout()
        self.fifth_row = QHBoxLayout()
        
        self.id_label = QLabel("ID :")
        self.id_label.setFont(QFont("Tahoma",10))
        self.id_edit = QLineEdit()
        self.id_edit.setFont(QFont("Tahoma",12))
        self.id_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.id_edit.setFixedWidth(150)
        self.first_row.setAlignment(Qt.AlignHCenter)
        
        self.password_label = QLabel("Password :")
        self.password_label.setFont(QFont("Tahoma",10))
        self.password_edit = QLineEdit()
        self.password_edit.setFont(QFont("Tahoma",12))
        self.password_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.password_edit.setFixedWidth(150)
        
        self.name_label = QLabel("Name :")
        self.name_label.setFont(QFont("Tahoma",10))
        self.name_edit = QLineEdit()
        self.name_edit.setFont(QFont("Tahoma",12))
        self.name_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.name_edit.setFixedWidth(150)
        self.third_row.setAlignment(Qt.AlignHCenter)
        self.third_row.setContentsMargins(60,0,50,0)
        
        self.surname_label = QLabel("Surname :")
        self.surname_label.setFont(QFont("Tahoma",10))
        self.surname_edit = QLineEdit()
        self.surname_edit.setFont(QFont("Tahoma",12))
        self.surname_edit.setStyleSheet("QLineEdit::hover{background-color:#EFFFFF;}")
        self.surname_edit.setFixedWidth(150)
        self.fourth_row.setAlignment(Qt.AlignHCenter)
        self.fourth_row.setContentsMargins(60,0,50,0)
       
        self.save_button = QPushButton("Save")
        self.save_button.setFixedWidth(80)
        self.fifth_row.setContentsMargins(140,0,0,0)
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
        
        self.first_row.addWidget(self.name_label)
        self.first_row.addWidget(self.name_edit)
        self.first_row.setContentsMargins(60,0,50,0)
        
        self.second_row.addWidget(self.surname_label)
        self.second_row.addWidget(self.surname_edit)
        self.second_row.setContentsMargins(60,0,50,0)
        
        self.third_row.addWidget(self.id_label)
        self.third_row.addWidget(self.id_edit)        
        
        self.fourth_row.addWidget(self.password_label)
        self.fourth_row.addWidget(self.password_edit)
        
        self.fifth_row.addWidget(self.save_button)
        
        self.form.addRow(self.first_row)
        self.form.addRow(self.second_row)
        self.form.addRow(self.third_row)
        self.form.addRow(self.fourth_row)
        self.form.addRow(self.fifth_row)
        
        self.resize(300,500)
        
    def sign_users(self,e):
        
        self.connect = sqlite3.connect("customers.db")
        self.connect.execute(f"""insert into customers
                             (name,surname,id,password)
                             values('{self.name_edit.text()}','{self.surname_edit.text()}','{self.id_edit.text()}','{self.password_edit.text()}')""")
        
        self.connect.commit()
        self.connect.close()
        self.close()
        
class main(QWidget):
    def __init__(self):
        super().__init__()
       
       
       
        self.background_label = QLabel(self)
        self.pixmap = QPixmap('Main_Theme.jpg')  # Resmin dosya yolu
        self.background_label.setPixmap(self.pixmap)
        self.background_label.setGeometry(0, 0, 650,700)
        self.background_label.setStyleSheet("background-image: url('Main_Theme.jpg');")
        
        
        
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
        self.forgot_password.setStyleSheet("color:white")
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
        self.id_list = [row[2] for row in connect.execute("select * from customers")]
        self.password_list = [row[3] for row in connect.execute("select * from customers")]
        self.name_list = [row[0] for row in connect.execute("select * from customers")]
        self.surname_list = [row[1] for row in connect.execute("select * from customers")]
        
        self.name =self.name_list[self.id_list.index(self.id_edit.text())]
        self.surname = self.surname_list[self.id_list.index(self.id_edit.text())]
        
        try:
            if self.id_edit.text() in self.id_list and self.password_list[self.id_list.index(self.id_edit.text())] == self.password_edit.text():
                self.close()
                self.open_Main_Window = Main_Window(self.name,self.surname)
                
                self.open_Main_Window.show()
                
        except ValueError:
            if self.id_edit.text() not in self.id_list :
                self.id_edit.clear()
                self.id_edit.setPlaceholderText("id is wrong")
            if self.password_edit.text() not in self.password_list:
                self.password_edit.clear()
                self.password_edit.setPlaceholderText("password is wrong")
            if self.id_edit.text() =="":
                self.id_edit.setPlaceholderText("write id")
            if self.password_edit.text() =="":
                self.password_edit.setPlaceholderText("write id")
            
    def forgot_password_clicked(self,e):
        
        self.show_window = New_Password_Window()
        self.show_window.show()

class New_Password_Window(QWidget):
        
    def __init__(self):
        super().__init__()
        
        
        self.vbox = QVBoxLayout(self)
        self.form = QFormLayout()
        self.vbox.addLayout(self.form)
        self.form.setContentsMargins(0,100,0,0)
        
        
        self.first_row = QHBoxLayout()
        self.second_row = QHBoxLayout()
        self.third_row = QHBoxLayout()
        
        self.old_password_label = QLabel("Eski şifre :")
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
            
            self.connect = sqlite3.connect("customers.db")
            password_list = [row[3] for row in connect.execute("select * from customers")]
            
            if self.old_password_edit.text() in password_list:
                if self.old_password_edit.text() == self.new_password_edit.text():
                    self.old_password_edit.clear()
                    self.new_password_edit.clear()
                    self.old_password_edit.setPlaceholderText("Same password")
                    self.old_password_edit.setToolTip("Same password")
                    self.old_password_edit.setStyleSheet("color:red;")
                else:
                    self.connect.execute(f"update customers set password = '{self.new_password_edit.text()}' where id ='{self.old_password_edit.text()}'")
                    self.save_button.close()
                    self.succes_label = QLabel("şifre sifirlandi")
                    self.succes_label.setStyleSheet("color: green;")
                    self.third_row.addWidget(self.succes_label)
                    self.timer = QTimer(self)
                    self.timer.timeout.connect(self.close)
                    self.timer.start(1000)
            
            else:
                self.old_password_edit.clear()
                self.old_password_edit.setPlaceholderText("ERROR!")
                self.old_password_edit.setStyleSheet("color:red;")
            self.connect.commit()
            self.connect.close()
             
class Main_Window(QMainWindow):
    
    def __init__(self,name,surname):
        super().__init__()
        self.name = name
        self.surname = surname
            
        self.menubar = self.menuBar()
        self.menubar.setFixedHeight(50)
        self.menubar.setStyleSheet(
                "QMenuBar {"
                "color:white;"
                "background-color: #018000;"
                "}"
                "QMenuBar::item {"
                "padding: 15px;"
                "}"
                "QMenuBar::item:selected {"
                "background-color: #5EBF00;"
                "}"
            )

        self.transfer_menu = self.menubar.addMenu('TRANSFER')
        self.account_menu = self.menubar.addMenu('HESAP')
        self.invest_menu = self.menubar.addMenu('YATIRIM')
            
        self.profil_label = QLabel(f"{self.name} {self.surname}")
        self.profil_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.profil_label.setStyleSheet("QLabel { color: white; padding:15px; } QLabel::hover { background-color: #5EBF00; }")
        self.profil_label.setFont(QFont("Tahoma",12))
        
        self.off_button = QPushButton()
        self.off_button.setIcon(QIcon("close.png"))
        self.off_button.clicked.connect(self.close)
        
        
        self.profil_widget = QWidget()
        self.profil_layout = QHBoxLayout(self.profil_widget)
        self.profil_layout.addWidget(self.profil_label)
        self.profil_layout.addWidget(self.off_button)
        self.profil_layout.setContentsMargins(0, 0, 10, 0)  
        self.profil_layout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        self.extra_content = QWidget()
        self.extra_layout = QVBoxLayout(self.extra_content)
        self.extra_layout.addWidget(self.profil_widget)
        
        self.profil_label.mousePressEvent = self.profile_clicked
        self.transfer_menu.triggered.connect(self.transfer_clicked) 
        self.invest_menu.triggered.connect(self.invest_menu_clicked) 
        self.account_menu.triggered.connect(self.account_clicked) 
        
        
        self.central_widget = QWidget(self)
        self.central_layout = QVBoxLayout()
        self.central_layout.addWidget(self.extra_content)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        
        self.setMenuBar(self.menubar)
        self.menubar.setCornerWidget(self.profil_widget)  
        self.resize(600, 600)
    
    def profile_clicked(self,e):
        self.extra_content.setStyleSheet("background-color: red;")

    def transfer_clicked(self,e):
        self.extra_content.setStyleSheet("background-color: green;")

    def invest_menu_clicked(self,e):
        self.extra_content.setStyleSheet("background-color: blue;")
        
    def account_clicked(self,e):
        self.extra_content.setStyleSheet("background-color: yellow;")

app = QApplication([])
window = main()
app.exec()