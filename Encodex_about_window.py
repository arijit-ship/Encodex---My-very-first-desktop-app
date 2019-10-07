# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Encodex_about_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 210)
        Dialog.setMinimumSize(QtCore.QSize(562, 210))
        Dialog.setMaximumSize(QtCore.QSize(562, 210))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 4, 481, 121))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 501, 41))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(221, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.label.setText(_translate("Dialog", "My name is Arijit Das. I am a sophomore in university. I don\'t know why I made this application. A whole bunch of online conversion tools is out there on the internet and you can do the same thing with those tools instead of using this stupid application. So I really appreciate that you put effort to install this application on your computer."))
        self.label_2.setText(_translate("Dialog", " Encodex Version 1.0.  (Sorry if the name is trademarked. Don\'t sue me, I will change it in upcoming version)"))
        self.pushButton.setText(_translate("Dialog", "Quit "))
