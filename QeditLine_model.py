"""
QLineEdit控件与回显模式
基本功能：输入单行的文本
EchoMode （回显模式）
4种回显模式
1. Normal
2. NoEcho
3.Password
4. PasswordEchoOnEdit

"""

import sys
from PyQt5.QtWidgets import *

class QEditlineModel(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("文本输入框的显示模式")

        # 表格布局
        formlayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnLineEdit = QLineEdit()

        formlayout.addRow("Normal", normalLineEdit)
        formlayout.addRow("NoEcho", noEchoLineEdit)
        formlayout.addRow("Passward", passwordLineEdit)
        formlayout.addRow("PasswordEchoOnEdit", passwordEchoOnLineEdit)

        # 框内灰色文字提示信息
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEdit")
        passwordEchoOnLineEdit.setPlaceholderText("PasswordEchoOnEdit")
        passwordLineEdit.setPlaceholderText("Passward")


        # 设置文本框模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QEditlineModel()
    mainWindow.show()
    sys.exit(app.exec_())