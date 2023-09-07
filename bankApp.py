from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.vbox= QVBoxLayout(self)
        self.hbox_logo = QHBoxLayout()
        self.form = QFormLayout(self)
        self.hbox_bottom  =QHBoxLayout()
        
        self.vbox.addLayout(self.hbox_logo)
        self.vbox.addLayout(self.form)
        self.vbox.addLayout(self.hbox_bottom)
        
        self.logo_label = QLabel(self)
        self.pixmap = QPixmap("bank_logo.jpg")
        self.scaled_pixmap = self.pixmap.scaled(100, 80)
        self.logo_label.setPixmap(self.scaled_pixmap)
        self.logo_label.setAlignment(Qt.AlignHCenter)
        
        
         
        self.hbox_logo.addWidget(self.logo_label)
        self.logo_label.setFixedSize(100, 200)
        
        self.label1 = QLabel("  Name :")
        self.edit1 = QLineEdit()
        self.edit1.setFixedWidth(200)
        self.label1.setContentsMargins(50,0,0,0)
        
        self.label2 = QLabel("Surname :")
        self.edit2 = QLineEdit()
        self.edit2.setFixedWidth(200)
        self.label2.setContentsMargins(50,0,0,0)
        
        self.button1 = QPushButton("login")
        self.button1.setFixedWidth(90)
        self.label3 = QLabel("forgot password")
        self.hbox_form = QHBoxLayout()
        self.hbox_form.addWidget(self.button1)
        self.hbox_form.addWidget(self.label3)
        self.hbox_form.setContentsMargins(50,0,0,0)
        self.hbox_form.setAlignment(Qt.AlignHCenter)
        
        self.form.addRow(self.label1 , self.edit1)
        self.form.addRow(self.label2 , self.edit2)
        self.form.addRow(self.hbox_form)
        
        
                
        
        
        self.resize(400,700)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()