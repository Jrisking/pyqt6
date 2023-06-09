"""
用掩码限制QLineEdit控件的输入
A            ASCII字母字符是必须输入的（A-Z、a-Z)

a            ASCII字母字符是允许输入的，但不是必需的（A-Z、a-z)

N            ASCII字母字符是必须输入的（A-Z、a-Z、0-9）

n            ASCII字母字符是允许输入的,但不是必需的（A-Z、a-z、0-9）
X            任何字符都是必须输入的

x            任何字符都是允许输入的，但不是必需的
9            ASCII数字字符是必须输入的（0-9）

0            ASCII数字字符是允许输入的，但不是必需的(0-9）


D           ASCII数字字符是必须输入的（1-9)
d            ASCII数字字符是允许输入的，但不是必需的（1-9)


#           ASCI数字字符或加减符号是允许输入的，但不是必需的
H            十六进制格式字符是必须输入的（A-F、a-f、0-9）

h            十六进制格式字符是允许输入的，但不是必需的（A-F、a-f、0-9)
B            二进制格式字符是必须输入的（0，1）

b            二进制格式字符是允许输入的，但不是必需的（0，1)
>           所有的字母字符都大写
"""

from PyQt5.QtWidgets import *
import sys

class LineeditMask(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QlineEdit控件的输入')
        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        ipLineEdit.setInputMask('000.000.000.000;_')  # ;后面表示如果没有输入就显示_
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dateLineEdit.setInputMask('0000-00-00;_')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        formLayout.addRow('数字掩码',ipLineEdit)
        formLayout.addRow('mac掩码',macLineEdit)
        formLayout.addRow('日期掩码',dateLineEdit)
        formLayout.addRow('许可证掩码',licenseLineEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = LineeditMask()
    mainWindow.show()
    sys.exit(app.exec_())
