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
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        result = float(first_count) + float(second_count)
        print(result)
        form.label_5.setText("%s" %result)
    except ValueError:
        form.label_5.setText("Проверьте корректность введенных данных")
    
def click_minus():
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        result = float(first_count) - float(second_count)
        print(result)
        form.label_5.setText("%s" %result)
    except ValueError:
        form.label_5.setText("Проверьте корректность введенных данных")

def click_multiply():
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        result = float(first_count) * float(second_count)
        print(result)
        form.label_5.setText("%s" %result)
    except ValueError:
        form.label_5.setText("Проверьте корректность введенных данных")

def click_simple_division():
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        result = float(first_count) / float(second_count)
        print(result)
        form.label_5.setText("%s" %result)
    except ZeroDivisionError:
        form.label_5.setText('На ноль делить нельзя')
    except ValueError:
        form.label_5.setText("Проверьте корректность введенных данных")

def click_whole_division():
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        result = float(first_count) // float(second_count)
        print(result)
        form.label_5.setText("целая часть от деления: %s" %result)
    except ZeroDivisionError:
        form.label_5.setText('На ноль делить нельзя')
    except ValueError:
        form.label_5.setText("Проверьте корректность введенных данных")

def click_residual_division():
    try:
        first_count = form.textEdit.toPlainText()
        second_count = form.textEdit_2.toPlainText()
        result = float(first_count) % float(second_count)
        print(result)
        form.label_5.setText("остаток от деления: %s" %result)
    except ZeroDivisionError:
        form.label_5.setText('На ноль делить нельзя')
    except ValueError:
        form.label_5.setText("Проверьте корректность введенных данных")
    

form.pushButton.clicked.connect(click_plus)
form.pushButton_2.clicked.connect(click_minus)
form.pushButton_3.clicked.connect(click_multiply)
form.pushButton_4.clicked.connect(click_simple_division)
form.pushButton_5.clicked.connect(click_whole_division)
form.pushButton_6.clicked.connect(click_residual_division)


app.exec_()
