
"""

创建和使用菜单

"""



import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        self.initUI()

    def initUI(self):
        bar = self.menuBar()

        file = bar.addMenu("文件")
        file.addAction("新建")

        save = QAction("保存", self)
        save.setShortcut("Command + S")  # 设置快捷键
        file.addAction(save)

        save.triggered.connect(self.process)   # triggered是引发的意思

        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("Quit", self)
        file.addAction(quit)

    def process(self):
        print(self.sender().text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MenuDemo()
    mainWindow.show()
    sys.exit(app.exec_())