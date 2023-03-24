# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinMenuToolBar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setCheckable(True)
        self.actionnew.setObjectName("actionnew")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionrecent_file = QtWidgets.QAction(MainWindow)
        self.actionrecent_file.setObjectName("actionrecent_file")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionrecent_file)
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionclose)
        self.menubar.addAction(self.menufile.menuAction())
        self.toolBar.addAction(self.actionnew)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionrecent_file)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionsave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionclose)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        self.actionrecent_file.setText(_translate("MainWindow", "最近文件"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionclose.setText(_translate("MainWindow", "close"))

