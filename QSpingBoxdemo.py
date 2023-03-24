"""
计数器控件
QSpinBox

该滑块的其他功能可以进去类里面之间看：比如范围，最大值最小值，默认值, 步长等等
"""

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Qspanbox(QWidget):
    def __init__(self):
        super(Qspanbox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSinBox计数器演示')
        self.resize(300,100)

        layout = QVBoxLayout()
        self.label = QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.sb = QSpinBox()
        self.sb.setValue(18)
        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(self.valueChange)

        self.setLayout(layout)

    def valueChange(self):
        self.label.setText('当前值：'+ str(self.sb.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Qspanbox()
    mainWindow.show()
    sys.exit(app.exec_())