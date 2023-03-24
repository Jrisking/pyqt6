
import sys
from PyQt5.QtWidgets import *

class Qtextdit(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QtestEdit控件演示")

        self.resize(300,200)

        self.textedit = QTextEdit()
        self.buttontext = QPushButton("显示文本")
        self.buttonHTML = QPushButton("显示HTML")

        layout = QVBoxLayout()
        layout.addWidget(self.textedit)
        layout.addWidget(self.buttontext)
        layout.addWidget(self.buttonHTML)

        self.buttontext.clicked.connect(self.onclick_buttontest)   # 注意连接函数不能加()
        self.buttonHTML.clicked.connect(self.onclick_buttonHTML)

        self.setLayout(layout)

    def onclick_buttontest(self):
        self.textedit.setPlainText('hello, world！')

    def onclick_buttonHTML(self):
        self.textedit.setHtml("<font color='yellow' size=6>你好，世界</font>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Qtextdit()
    mainWindow.show()
    sys.exit(app.exec_())