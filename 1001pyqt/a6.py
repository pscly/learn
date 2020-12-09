# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction, QStatusBar, QCheckBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon



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
        toolbar.setIconSize(QSize(16, 16))  # 这个是在PyQt5.AtCore引入QtCore
        self.addToolBar(toolbar)

        # TODO 引入QAction
        # QSIZE那个是可选项， 而且需要引入
        button_action = QAction(QIcon('bug.png'), "按钮1", self)   # 这样就是有个图标
        # button_action1 = QAction("按钮2", self)    # 这样子就是没有图标

        # 这个图标在不同的系统下会有不同的情况

        button_action.setStatusTip("This is your button")   # 和下面的这东西搭配<01>
        # button_action1.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)    # 这个表示如果点击，去执行哪个函数
        # button_action1.triggered.connect(self.onMyToolBarButtonClick)    # 这个表示如果点击，去执行哪个函数

        button_action.setCheckable(True)    # 将按钮变成切换的那种按钮(就可以点击时知道当前的状态)

        toolbar.addAction(button_action)    # 吧按钮渲染到工具栏Toolbar
        # toolbar.addAction(button_action1)


        # # # 3 的最后一个任务
        button_action2 = QAction(QIcon("bug.png"), "Your button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)

        toolbar.addAction(button_action2)



        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())    # QCheckBox 需要引入




        self.setStatusBar(QStatusBar(self)) #TODO 引入QStatusBar # 和上面搭配<01>

    def onMyToolBarButtonClick(self, s):
        print("click 点击", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()