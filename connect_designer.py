import sys
# import untitled   # 取消本地库导入的方法，左侧右击目录：标记目录为资源：根
import MainWinMenuToolBar
from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinMenuToolBar.Ui_MainWindow()
    # 往主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())