"""
单选框控件 QRadioButton


"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Qradiobutton(QWidget):
    def __init__(self):
        super(Qradiobutton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("单选框测试")
        layout = QHBoxLayout()
        self.button1 = QRadioButton("单选按钮1")
        self.button1.setChecked(True)

        self.button1.toggled.connect(self.buttonstate)   # toggled: 切换状态
        layout.addWidget(self.button1)

        self.button2 = QRadioButton("单选按钮2")

        self.button2.toggled.connect(self.buttonstate)
        layout.addWidget(self.button2)

        self.setLayout(layout)


    def buttonstate(self):
        radiobutton = self.sender()
        if radiobutton.text() == '单选按钮1':
            if radiobutton.isEnabled() == True:
                print('<' + radiobutton.text() + '> 被选中')
            else:
                print('<' + radiobutton.text() + '> 取消被选中')
        if radiobutton.text() == '单选按钮2':
            if radiobutton.isEnabled() == True:
                print('<' + radiobutton.text() + '> 被选中')
            else:
                print('<' + radiobutton.text() + '> 取消被选中')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Qradiobutton()
    mainWindow.show()
    sys.exit(app.exec_())