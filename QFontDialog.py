"""

字体对话框： QFontDialog, 调出字体对话框，供我们选择字体

"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QFontdialogdemo(QWidget):
    def __init__(self):
        super(QFontdialogdemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QFontdialogdemo演示")
        self.resize(300,400)
        layout = QVBoxLayout()

        self.fontbotton = QPushButton('选择字体')
        self.fontbotton.clicked.connect(self.getFont)
        layout.addWidget(self.fontbotton)

        self.fontLabel = QLabel("Hello, 测试字体例子")
        layout.addWidget(self.fontLabel)

        self.setLayout(layout)

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)  # 改变字体




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QFontdialogdemo()
    mainWindow.show()
    sys.exit(app.exec_())