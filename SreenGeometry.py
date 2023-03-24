import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget



def onClick_Button():
    # print("onclick")
    print("这是整个窗口的坐标和内容框的大小")
    print("widge.x() = %d" % widget.x())
    print("widge.y() = %d" % widget.y())
    print("widge.width() = %d" % widget.width())
    print("widge.height() = %d" % widget.height())

    print("这是窗口内容区域的坐标和大小")
    print("widge.geometry().x() = %d" % widget.geometry().x())
    print("widge.geometry().y() = %d" % widget.geometry().y())
    print("widge.geometry().width() = %d" % widget.geometry().width())
    print("widge.geometry().height() = %d" % widget.geometry().height())

    print("这是整个窗口的坐标和大小")
    print("widge.frameGeometry().x() = %d" % widget.frameGeometry().x())
    print("widge.frameGeometry().y() = %d" % widget.frameGeometry().y())
    print("widge.frameGeometry().width() = %d" % widget.frameGeometry().width())
    print("widge.frameGeometry().height() = %d" % widget.frameGeometry().height())

app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)

btn.move(24, 52)

widget.resize(300,240)  # 窗口大小， 这是工作区的宽高

widget.move(250, 250)  # 将窗口移动在距离屏幕左上角250的位置

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())