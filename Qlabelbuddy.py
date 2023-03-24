
"""

主动添加热键
"""

import sys
from PyQt5.QtWidgets import *

class QlabelBuddy(QDialog): # 这个基类是一个对话框，没有说什么选项栏什么的
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Qlabel与伙伴控件')

        namelabel = QLabel('&Name',self)
        namelineedit = QLineEdit(self)

        # 设置伙伴关系
        namelabel.setBuddy(namelineedit)


        pwdlabel = QLabel('&Pwd', self)
        pwdedit = QLineEdit(self)

        # 设置伙伴关系
        pwdlabel.setBuddy(pwdedit)

        btnOK = QPushButton('&OK')
        btncancel = QPushButton('&Cancel')

        # 栅格布局
        mainlayout = QGridLayout(self)
        mainlayout.addWidget(namelabel,0,0)
        mainlayout.addWidget(namelineedit,0,1,1,2)

        mainlayout.addWidget(pwdlabel,1,0)
        mainlayout.addWidget(pwdedit,1,1,1,2)

        mainlayout.addWidget(btnOK,2,2)
        mainlayout.addWidget(btncancel,2,1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QlabelBuddy()
    mainWindow.show()
    sys.exit(app.exec_())