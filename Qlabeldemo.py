"""
QLabel控件
setAlignment()：设置文本的对齐方式
setIndent()：设置文本缩进
text()：获取文本内容
setBuddy()：设置伙伴关系I
setText()：设置文本内容
selectedText()：返回所选择的字符
setWordWrap()：设置是否允许换行

QtCore 的 Qt

QLabel常用的信号（事件）：
1. 当鼠标滑过QLabel控件时触发：linkHovered
2. 当鼠标单击QLabel控件时触发：linkActivated

"""

import sys
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPalette # 调色板
from PyQt5.QtCore import Qt

class Qlabeldemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter) # 设置文本对齐方式

        label2.setText("<a href='www.baidu.com'>百度一下</a>")
        label2.setToolTip("这是一个超链接")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./0001TP_006690.png"))

        # 设置为ture，则点击事件用浏览器打开网页
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='www.jd.com'>京东主页</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接")

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)
        self.setLayout(vbox)


    def linkHovered(self):
        print('鼠标已划过标签为2，触发事件2')

    def linkClicked(self):
        print('鼠标已划过标签为4，触发事件4')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Qlabeldemo()
    mainWindow.show()
    sys.exit(app.exec_())



