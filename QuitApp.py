import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget   # 分别是水平布局， 主窗口， 创建应用，添加按钮

class QuitApp(QMainWindow):
    def __init__(self):
        super(QuitApp, self).__init__()
        self.resize(300,120)
        self.setWindowTitle('推出应用')
        # 添加按钮
        self.button1 = QPushButton('点击退出')
        # 点击之后出发动作
        self.button1.clicked.connect(self.onClick_button)

        # 按钮水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe = QWidget()
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)

    def onClick_button(self):
        # 创建信号
        sender = self.sender()
        print(sender.text() + '已点击按钮')
        app = QApplication.instance()

        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon())  # 设置程序图标
    main = QuitApp()
    main.show()
    sys.exit(app.exec_())