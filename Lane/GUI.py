# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
 
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 400)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        Dialog.setMaximumSize(QtCore.QSize(400, 400))
       
        #GroupBox1
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 381, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 62, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        #Choose Input Path
        self.InputChoose = QtGui.QPushButton(self.groupBox)
        self.InputChoose.setGeometry(QtCore.QRect(320, 28, 40, 25))
        self.InputChoose.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.InputChoose.setObjectName(_fromUtf8("InputChoose"))
        self.txtPath1 = QtGui.QLineEdit(self.groupBox)
        self.txtPath1.setGeometry(QtCore.QRect(70, 30, 241, 20))
        self.txtPath1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtPath1.setReadOnly(True)
        self.txtPath1.setObjectName(_fromUtf8("txtPath1"))
        #Choose Output Path
        self.OutputChoose = QtGui.QPushButton(self.groupBox)
        self.OutputChoose.setGeometry(QtCore.QRect(320, 58, 40, 25))
        self.OutputChoose.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.OutputChoose.setObjectName(_fromUtf8("OutputChoose"))
        self.txtPath2 = QtGui.QLineEdit(self.groupBox)
        self.txtPath2.setGeometry(QtCore.QRect(70, 60, 241, 20))
        self.txtPath2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtPath2.setReadOnly(True)
        self.txtPath2.setObjectName(_fromUtf8("txtPath2"))
        
        #Choose Mode Button
        self.btnLight = QtGui.QPushButton(Dialog)
        self.btnLight.setGeometry(QtCore.QRect(10, 280, 381, 51))
        self.btnLight.setObjectName(_fromUtf8("btnLight"))
        
        self.btnDark = QtGui.QPushButton(Dialog)
        self.btnDark.setGeometry(QtCore.QRect(10, 340, 381, 51))
        self.btnDark.setObjectName(_fromUtf8("btnDark"))
    
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "车道标线识别程序 by Rowling", None))
        self.btnLight.setText(_translate("Dialog", "光亮模式", None))
        self.btnDark.setText(_translate("Dialog", "昏暗模式", None))
        self.groupBox.setTitle(_translate("Dialog", "请选择需要处理的图片文件夹以及输出图片的存放位置", None))
        self.label_2.setText(_translate("Dialog", "输出", None))
        self.InputChoose.setText(_translate("Dialog", "...", None))
        self.OutputChoose.setText(_translate("Dialog", "...", None))
    
   
       
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    