# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 255, 32))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: cadetblue;")
        self.label.setObjectName("label")
        self.password_lbl = QtWidgets.QLabel(self.centralwidget)
        self.password_lbl.setGeometry(QtCore.QRect(90, 150, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.password_lbl.setFont(font)
        self.password_lbl.setObjectName("password_lbl")
        self.generate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generate_btn.setGeometry(QtCore.QRect(80, 200, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.generate_btn.setFont(font)
        self.generate_btn.setStyleSheet("background-color: cadetblue;\n"
"color: black;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.generate_btn.setObjectName("generate_btn")
        self.use_upper = QtWidgets.QCheckBox(self.centralwidget)
        self.use_upper.setGeometry(QtCore.QRect(10, 60, 143, 26))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.use_upper.setFont(font)
        self.use_upper.setObjectName("use_upper")
        self.use_lower = QtWidgets.QCheckBox(self.centralwidget)
        self.use_lower.setGeometry(QtCore.QRect(10, 100, 119, 26))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.use_lower.setFont(font)
        self.use_lower.setObjectName("use_lower")
        self.use_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.use_numbers.setGeometry(QtCore.QRect(170, 60, 85, 26))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.use_numbers.setFont(font)
        self.use_numbers.setObjectName("use_numbers")
        self.use_symbols = QtWidgets.QCheckBox(self.centralwidget)
        self.use_symbols.setGeometry(QtCore.QRect(170, 100, 97, 26))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.use_symbols.setFont(font)
        self.use_symbols.setObjectName("use_symbols")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Генератор паролів"))
        self.password_lbl.setText(_translate("MainWindow", "Пароль"))
        self.generate_btn.setText(_translate("MainWindow", "Генерувати"))
        self.use_upper.setText(_translate("MainWindow", "Великі букви"))
        self.use_lower.setText(_translate("MainWindow", "Малі букви"))
        self.use_numbers.setText(_translate("MainWindow", "Цифри"))
        self.use_symbols.setText(_translate("MainWindow", "Символи"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
