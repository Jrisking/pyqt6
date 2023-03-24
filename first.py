import sys
from PyQt5.QtWidgets import QApplication, QWidget



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(400,200)
    window.move(300,300)
    window.setWindowTitle('深度废物')
    window.show()
    sys.exit(app.exec_())