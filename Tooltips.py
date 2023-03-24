import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget, QToolTip # 按钮提示信息
from PyQt5.QtGui import QFont

class Tooltip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天的天气真好')
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('设置窗口的提示信息')

        self.button1 = QPushButton('QUIT')
        self.button1.setToolTip('确定需要关闭吗')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Tooltip()
    # ui = Tooltip.Ui_MainWindow()Tooltip
    # 往主窗口添加控件
    # ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())