# -*- coding: utf-8 -*-
 
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
 
import Fill
from GUI import Ui_Dialog
 
class ImageProcess(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.exclude_list = []
    
    @QtCore.pyqtSignature("")
    def on_InputChoose_clicked(self):
        self.indir = QtGui.QFileDialog.getExistingDirectory(self,  u"选择目录","../photos/light_lane").replace("\\","/")
        self.txtPath1.setText(self.indir)
    
    @QtCore.pyqtSignature("")
    def on_OutputChoose_clicked(self):
        self.outdir = QtGui.QFileDialog.getExistingDirectory(self,  u"选择目录","../result/laneresult").replace("\\","/")
        self.txtPath2.setText(self.outdir)
 
   
    @QtCore.pyqtSignature("")
    def on_btnLight_clicked(self):
        Fill.processLightLane(str(self.indir),str(self.outdir))
        QtGui.QMessageBox.warning(self, '完成', '处理完毕，请到输出目录下查看')
    
     
    @QtCore.pyqtSignature("")
    def on_btnDark_clicked(self):
        Fill.processDarkLane(str(self.indir),str(self.outdir))
        QtGui.QMessageBox.warning(self, '完成', '处理完毕，请到输出目录下查看')
        
    def get_formated_path1(self):
        return self.format_path(self.txtPath1.text())
        
    def get_formated_path2(self):
        return self.format_path(self.txtPath2.text())
        
    def format_path(self, path):
        return str(path).rstrip('\\') + '\\'
 
 
if __name__ == "__main__":
    reload(sys)
    app = QtGui.QApplication(sys.argv)
    dlg = ImageProcess()
    dlg.show()
    sys.exit(app.exec_())
 