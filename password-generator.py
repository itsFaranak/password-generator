
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSpinBox, QPushButton, QLineEdit, QMessageBox
from PyQt5 import uic
import random
from PyQt5.QtGui import QClipboard

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # Load the UI file
        uic.loadUi("password-generator.ui", self)
        self.setWindowTitle("Password Generator")

        # Define our widgets
        self.label_title = self.findChild(QLabel, "label_title")
        self.label_length = self.findChild(QLabel, "label_length")
        self.spin_length = self.findChild(QSpinBox, "spin_length")
        self.generate_button = self.findChild(QPushButton, "generate_button")
        self.copy_button = self.findChild(QPushButton, "copy_button")
        self.line_password = self.findChild(QLineEdit, "line_password")

        # Create Spin box
        self.spin_length.setMinimum(10)
        self.spin_length.setMaximum(65)
        self.spin_length.setValue(16)

        # click button signals
        self.generate_button.clicked.connect(self.new_password)
        self.copy_button.clicked.connect(self.copy_password)

        # Show the App
        self.show()

    def new_password(self):

        length = self.spin_length.value()

        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "/*-+.=-_()&^%$#@!~{}[]:;'?><`"

        password = [random.choice(lower),
                    random.choice(upper),
                    random.choice(numbers),
                    random.choice(symbols)]

        all_char = lower + upper + numbers + symbols
        for i in range(length - 4):
            password += (random.choices(all_char))
            random.shuffle(password)
            final_password = "".join(password)
            self.line_password.setText(final_password)

    def copy_password(self):
        if self.line_password.text():
            # copy that password to the clipboard
            QApplication.clipboard().setText(self.line_password.text())

            QMessageBox.information(self, "Success" ,"Password copied to clipboard!")
        else:
            QMessageBox.warning(self, "Sorry","No password to copy!")


 #Initilize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()      

