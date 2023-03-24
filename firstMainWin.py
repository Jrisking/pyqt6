import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()

        # 设置主窗口标题
        self.setWindowTitle('深度废物')

        # 设置窗口尺寸
        self.resize(400,300)

        # 添加状态栏
        self.status = self.statusBar()

        # 状态栏显示信息
        self.status.showMessage('只存在5s', 5000)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon())  # 设置程序图标
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())