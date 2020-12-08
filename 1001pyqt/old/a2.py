import sys, time
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import Qt

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("窗口标题")

        label = QLabel("这是一个pyqt的窗口")

        # qt还有更多的插件http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)

class CustomButton(QPushButton):

    def keyPressEvent(self, e):
        # My custom event handling
        super(CustomButton, self).keyPressEvent(e)

app = QApplication(sys.argv)

window = MainWindow()       # 把这里替换为QWidget
window.show()


x = app.exec_()     # 启动窗口并且等待关闭, 关闭返回0(int)

