from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

css = """
    QLineEdit{border:none;}
    QLineEdit::focus{border-bottom: 1px solid skyblue}
    """
    


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.vbox = QVBoxLayout(self)
        
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        
        self.form1 = QFormLayout()
        self.form2 = QFormLayout()
        
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        
         
         
        self.label1 = QLabel("Username :")
        self.label1.setFont(QFont("Tahoma",10))
        self.label1.setContentsMargins(140,0,0,0)
        
        self.edit1 = QLineEdit()
        self.edit1.setFixedWidth(150)
        self.edit1.setFont(QFont("Tahoma",12))
        self.edit1.setStyleSheet(css)
        self.edit1.setContentsMargins(0,0,0,0)
        
        self.form1.addRow(self.label1,self.edit1)
        self.hbox1.addLayout(self.form1)
        self.hbox1.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        
        
        self.label2 = QLabel("Password :")
        self.label2.setContentsMargins(140,0,0,0)
        self.label2.setFont(QFont("Tahoma",10))
        
        self.edit2 = QLineEdit()
        self.edit2.setFixedWidth(150)
        self.edit2.setFont(QFont("Tahoma",12))
        self.edit2.setStyleSheet(css)
        self.edit2.setEchoMode(QLineEdit.Password)
        
        self.show_button = QPushButton()
        self.show_button.setIcon(QIcon("show_button.png"))
        
        
        self.form2.addRow(self.label2,self.edit2)
        self.hbox2.addLayout(self.form2)
        self.hbox2.addWidget(self.show_button)
        self.hbox2.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        
        
        
        
        
        
        
        
        self.resize(500,700)
        self.show()
        
app = QApplication([])
window = main()
app.exec()