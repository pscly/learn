# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：


import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

app = QApplication(sys.argv)
windows = QWidget()
windows.resize(500,500)
windows.move(100,100)

windows.setWindowTitle('Title')
# set icon
windows.setWindowIcon(QtGui.QIcon('a1.png'))
windows.show()
sys.exit(app.exec_())
