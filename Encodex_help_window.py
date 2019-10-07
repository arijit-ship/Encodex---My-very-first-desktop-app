# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Encodex_help_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 246)
        Dialog.setMinimumSize(QtCore.QSize(560, 246))
        Dialog.setMaximumSize(QtCore.QSize(560, 246))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 521, 151))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Encodex Help"))
        self.label.setText(_translate("Dialog", "This application is pretty straight forward. You have to enter some values in the input box using the virtual keys and to get corresponding ASCII, Binary or Hexadecimal value, press any of these operation buttons-- Get ASCII Value, Get Binary Value, Get Hex Value.\n"
"\n"
"Note:\n"
"For an integer value, \'Get Binary Value\' & \'Get Hex Value\' will return the Binary value and the Hexadecimal value of that integer respectively. But for a string (alphabet or alphanumeric string or special character), they will return the Binary value or the Hexadecimal value of the corresponding ASCII integer of the string(including digits)."))
        self.pushButton.setText(_translate("Dialog", "Quit Help"))
