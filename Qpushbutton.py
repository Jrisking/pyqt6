"""

这是所有的按钮控件类型
QAbstractButton
QPushButton
AToolButton
QRadioButton
QCheckBox

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QpushButton(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QpushButton_demo')
        self.resize(300,200)

        layout = QVBoxLayout()

        self.button1 = QPushButton("第一个按钮")
        # self.button1.setText('第一个')
        # 这两个是配对的，toggle按下去是不会弹起来，再按一次就弹起来
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))   # lamda表达式当做是一个槽，为什么需要lamda，因为connect需要发送一个信号，那么self.whichbutton就传不了参数了
        self.button1.clicked.connect(self.buttonstate)

        self.button2 = QPushButton("图像按钮")
        self.button2.setIcon(QIcon(QPixmap('./0001TP_006690.png')))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))

        # 设置不可用按钮
        self.button3 = QPushButton("不可用按钮")
        self.button3.setEnabled(False)

        # 设置默认项
        self.button4 = QPushButton("默认按钮")
        self.button4.setDefault(True)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def buttonstate(self):
        if self.button1.isCheckable():
            print('按钮1已被选中！！')
        else:
            print('按钮1未被选中！！')

    def whichButton(self, button):
        print('被单击的按钮是：' + button.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QpushButton()
    mainWindow.show()
    sys.exit(app.exec_())