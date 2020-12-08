# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) is fine.

app = QApplication(sys.argv)    # 可以是app = QApplication([])

window = QWidget()
window.show() # 重要！ 默认情况下窗口隐藏


# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.