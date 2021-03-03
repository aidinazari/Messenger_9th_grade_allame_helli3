# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window (copy).ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Menu(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Groups = QtWidgets.QListWidget(self.centralwidget)
        self.Groups.setGeometry(QtCore.QRect(25, 71, 661, 461))
        self.Groups.setObjectName("Groups")
        item = QtWidgets.QListWidgetItem()
        self.Groups.addItem(item)
        
        self.searchL = QtWidgets.QLineEdit(self.centralwidget)
        self.searchL.setGeometry(QtCore.QRect(20, 30, 251, 25))
        self.searchL.setInputMask("")
        self.searchL.setText("")
        self.searchL.setEchoMode(QtWidgets.QLineEdit.NoEcho)
        self.searchL.setObjectName("searchL")

        self.searchB = QtWidgets.QPushButton(self.centralwidget)
        self.searchB.setGeometry(QtCore.QRect(290, 30, 89, 25))
        self.searchB.setObjectName("searchB")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 22))
        self.menubar.setObjectName("menubar")

        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        MainWindow.setMenuBar(self.menubar)

        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")

        self.menuMenu.addAction(self.actionsetting)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.Groups.isSortingEnabled()
        self.Groups.setSortingEnabled(False)
        item = self.Groups.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        self.Groups.setSortingEnabled(__sortingEnabled)
        self.searchL.setPlaceholderText(_translate("MainWindow", "Search"))
        self.searchB.setText(_translate("MainWindow", "search"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionsetting.setText(_translate("MainWindow", "setting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Menu(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
