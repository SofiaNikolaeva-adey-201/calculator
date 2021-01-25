import pickle
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("calculator.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()



def click_plus():
    first_count = form.textEdit.toPlainText()
    second_count = form.textEdit_2.toPlainText()
    print(float(first_count) + float(second_count))


def click_minus():
    first_count = form.textEdit.toPlainText()
    second_count = form.textEdit_2.toPlainText()
    print(float(first_count) - float(second_count))

def click_multiply():
    first_count = form.textEdit.toPlainText()
    second_count = form.textEdit_2.toPlainText()
    print(float(first_count) * float(second_count))

def click_simple_division():
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        print(float(first_count) / float(second_count))
    except ZeroDivisionError:
        print('На ноль делить нельзя')


def click_whole_division():
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        print(float(first_count) // float(second_count))
    except ZeroDivisionError:
        print('На ноль делить нельзя')

def click_residual_division():
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        print(float(first_count) % float(second_count))
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    



form.pushButton.clicked.connect(click_plus)
form.pushButton_2.clicked.connect(click_minus)
form.pushButton_3.clicked.connect(click_multiply)
form.pushButton_4.clicked.connect(click_simple_division)
form.pushButton_5.clicked.connect(click_whole_division)
form.pushButton_6.clicked.connect(click_residual_division)




app.exec_()
