"""

颜色对话框： QColorDialog, 调出颜色对话框，供我们选择颜色

"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QColordialogdemo(QWidget):
    def __init__(self):
        super(QColordialogdemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QColordialogdemo演示")
        self.resize(300,400)
        layout = QVBoxLayout()

        self.Colorbotton = QPushButton('选择颜色')
        self.Colorbotton.clicked.connect(self.getColor)
        layout.addWidget(self.Colorbotton)

        self.ColorLabel = QLabel("Hello, 测试颜色例子")
        layout.addWidget(self.ColorLabel)

        self.setLayout(layout)

    def getColor(self):
        Color = QColorDialog.getColor()  # 只返回一个值
        p = QPalette()
        p.setColor(QPalette.WindowText, Color)  # 注意大小写
        self.ColorLabel.setPalette(p)    # 设置字体颜色。此外，设置背景颜色的功能是： self.colorLabel.setAutoFillBackground(True)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QColordialogdemo()
    mainWindow.show()
    sys.exit(app.exec_())