import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()

        # 设置主窗口标题
        self.setWindowTitle('深度废物')

        # 设置窗口尺寸
        self.resize(400,300)

    def center(self):
        # 获取屏幕坐标
        screen = self.QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        # 计算新的坐标
        newleft = (screen.width() - size.width()) / 2
        newtop = (screen.height() - size.height()) / 2
        self.move(newleft, newtop)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon())  # 设置程序图标
    main = CenterForm()
    main.show()

    sys.exit(app.exec_()) 