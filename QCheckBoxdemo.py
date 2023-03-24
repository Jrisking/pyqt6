"""
复选框按钮
QCheckBox

有三种状态
未选中 0

半选中 1

选中 2

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QCheckboxdemo(QWidget):

    def __init__(self):
        super(QCheckboxdemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("复选框控件演示")
        self.resize(300,200)

        layout = QHBoxLayout()

        self.checkbox1 = QCheckBox('复选框控件1')
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda:self.checkboxstate(self.checkbox1))

        self.checkbox2 = QCheckBox('复选框控件2')
        self.checkbox2.stateChanged.connect(lambda:self.checkboxstate(self.checkbox2))

        # 半选框
        self.checkbox3 = QCheckBox('半选框控件3')
        self.checkbox3.stateChanged.connect(lambda:self.checkboxstate(self.checkbox3))
        self.checkbox3.setTristate(True)   # 这个设为true，才能处于半选中状态
        self.checkbox3.setCheckState(Qt.PartiallyChecked)

        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.checkbox3)
        self.setLayout(layout)

    def checkboxstate(self, cb):
        check1status = self.checkbox1.text() + ', ischeck=' + str(self.checkbox1.isChecked()) + ',checkstate' + str(self.checkbox1.checkState()) + '\n'
        check2status = self.checkbox2.text() + ', ischeck=' + str(self.checkbox2.isChecked()) + ',checkstate' + str(self.checkbox2.checkState()) + '\n'
        check3status = self.checkbox3.text() + ', ischeck=' + str(self.checkbox3.isChecked()) + ',checkstate' + str(self.checkbox3.checkState()) + '\n'
        print(check1status + check2status + check3status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QCheckboxdemo()
    mainWindow.show()
    sys.exit(app.exec_())