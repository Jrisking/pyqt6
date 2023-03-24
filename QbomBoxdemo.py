"""

下拉列表控件（QComboBox）
1.如果将列表项添加到QComboBox控件中
2.如何获取选中的列表项


"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QBombox(QWidget):
    def __init__(self):
        super(QBombox,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(300,100)
        self.label1 = QLabel("请选择编程语言")
        self.label2 = QLabel("你选择的是第1种语言")

        layout = QVBoxLayout()

        self.cb = QComboBox()   # 下拉列表控件
        self.cb.addItem('C++')
        self.cb.addItems(["python", "Java", "Go", "C#"])

        self.cb.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.label1)
        layout.addWidget(self.cb)
        layout.addWidget(self.label2)
        self.setLayout(layout)


    def selectionChange(self, i):  # 这个i 是什么？ 下拉框的索引值
        self.label2.setText("你选择的是第{}种语言".format(int(self.cb.currentIndex())+1))  # 改变了self.label的值
        self.label2.adjustSize()

        for count in range(self.cb.count()):
            print('item'+str(count)+'='+self.cb.itemText(count))
            print('current index', i, 'selection changed', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QBombox()
    mainWindow.show()
    sys.exit(app.exec_())