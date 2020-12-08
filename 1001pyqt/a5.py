# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction, QStatusBar
from PyQt5.QtCore import Qt



# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        # 上面添加了一堆工具栏
        # QToolBar 需要引入
        toolbar = QToolBar("显示工具栏")   # 这个是右键点出的东西(目前是删除了就无法恢复)
        self.addToolBar(toolbar)

        button_action = QAction("按钮1", self)    #TODO 引入QAction
        # button_action1 = QAction("按钮2", self)    #TODO 引入QAction
        button_action.setStatusTip("This is your button")   # 和下面的这东西搭配
        # button_action1.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)    # 这个表示如果点击，去执行哪个函数
        # button_action1.triggered.connect(self.onMyToolBarButtonClick)    # 这个表示如果点击，去执行哪个函数

        button_action.setCheckable(True)    # 将按钮变成切换的那种按钮(就可以知道当前的状态)

        toolbar.addAction(button_action)    # 吧按钮渲染到工具栏Toolbar
        # toolbar.addAction(button_action1)

        self.setStatusBar(QStatusBar(self)) #TODO 引入QStatusBar

    def onMyToolBarButtonClick(self, s):
        print("click 点击", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()