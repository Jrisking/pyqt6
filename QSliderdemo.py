"""
滑块控件QSlider

"""

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Qsliderdemo(QWidget):
    def __init__(self):
        super(Qsliderdemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(300,100)

        layout = QVBoxLayout()
        self.label = QLabel('hello, pyqt5')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)

