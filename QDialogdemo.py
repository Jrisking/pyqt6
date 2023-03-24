"""

对话框：QDialog
OMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog

OMainWindow
QWidget
QDialog

"""

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QDialogdemo(QMainWindow):
    def __init__(self):
        super(QDialogdemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.button = QPushButton(self)  # 一定要点self,否则失败，不会显示
        self.button.setText('点击弹出')
        self.button.move(50,50)
        self.button.clicked.connect(self.showDialog)

        # layout = QVBoxLayout()
        # layout.addWidget(self.button)
        # self.setLayout(layout)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')

        # 但这个对话激活时，主对话框变灰，不能点击
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QDialogdemo()
    mainWindow.show()
    sys.exit(app.exec_())