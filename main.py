from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.generate_btn.clicked.connect(self.passgen)

    def passgen(self):
        lower = "qwertyuiopasdfghjklzxcvbnm"
        upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        numbers = "0123456789"
        symbols = "!@#$%^&*()_+}{:|;<>?/.,"

        characters_set = ""

        if self.ui.use_lower.isChecked():
            characters_set += lower
        if self.ui.use_upper.isChecked():
            characters_set += upper
        if self.ui.use_numbers.isChecked():
            characters_set += numbers
        if self.ui.use_symbols.isChecked():
            characters_set += symbols

        result = ""
        number = random.randint(8, 16)
        for i in range(number):
            try:
                result += random.choice(characters_set)
            except IndexError:
                print("Виберіть щось зі списку!!!")
                break
        self.ui.password_lbl.setText(result)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()