
"""
现在QLineEdit控件的输入（校验器）
如限制只能输入整数、浮点数或满足一定条件的字符串

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp

class Qlineeditvalidator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 创建表单布局
        formLayout = QFormLayout()

        # 创建框框
        intlineedit = QLineEdit()
        doublelineedit = QLineEdit()
        validatoredit = QLineEdit()

        formLayout.addRow('整数类型', intlineedit)
        formLayout.addRow('浮点类型', doublelineedit)
        formLayout.addRow('字母和数字', validatoredit)

        # 设置阴影提示
        intlineedit.setPlaceholderText('整数')
        doublelineedit.setPlaceholderText('浮点数')
        validatoredit.setPlaceholderText('数字和字母')

        # 整数校验器 [1,99]
        intvalidator = QIntValidator(self)
        intvalidator.setRange(1,99)

        doublevalidator = QDoubleValidator(self)
        doublevalidator.setRange(-360,360)
        doublevalidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度
        doublevalidator.setDecimals(2)

        # 字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        intlineedit.setValidator(intvalidator)
        doublelineedit.setValidator(doublevalidator)
        validatoredit.setValidator(validator)

        self.setLayout(formLayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Qlineeditvalidator()
    mainWindow.show()
    sys.exit(app.exec_())

