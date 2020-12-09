# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：  自己有空的时候弄得
import sys, time
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction, QStatusBar
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.resize(600, 500)
        self.move(0, 0)
        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")  # 设置窗口内部内容1     # 这个需要使用对其，不然就是中间，从左到右
        label.setAlignment(Qt.AlignCenter)  # 这个窗口使用什么对齐

        self.setCentralWidget(label)  # 将渲染

        # 上面添加了一堆工具栏
        # QToolBar 需要引入
        toolbar = QToolBar("显示工具栏")  # 这个是右键点出的东西(目前是删除了就无法恢复)
        toolbar.setIconSize(QSize(32, 32))  # 这个是在PyQt5.AtCore引入QtCore
        self.addToolBar(toolbar)

        # TODO 引入QAction
        # QSIZE那个是可选项， 而且需要引入
        button_action = QAction(QIcon('bug.png'), "按钮1", self)  # 这样就是有个图标
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)      # 更改为显示 图标+文字
        # Qt.ToolButtonIconOnly	            仅图标，无文本
        # Qt.ToolButtonTextOnly	            仅文本，无图标
        # Qt.ToolButtonTextBesideIcon	    图标和文本，图标旁边有文本
        # Qt.ToolButtonTextUnderIcon	    图标和文本，图标下有文本
        # Qt.ToolButtonFollowStyle	        遵循主机桌面样式


        # button_action = QAction( "按钮1", self)  # 这样就是有个图标
        # button_action1 = QAction("按钮2", self)    # 这样子就是没有图标

        # 这个图标在不同的系统下会有不同的情况

        button_action.setStatusTip("This is your button")  # 和下面的这东西搭配<01>
        # button_action1.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)  # 这个表示如果点击，去执行哪个函数
        # button_action1.triggered.connect(self.onMyToolBarButtonClick)    # 这个表示如果点击，去执行哪个函数



        button_action.setCheckable(True)  # 将按钮变成切换的那种按钮(就可以点击时知道当前的状态)

        toolbar.addAction(button_action)  # 吧按钮渲染到工具栏Toolbar
        # toolbar.addAction(button_action1)

        self.setStatusBar(QStatusBar(self))  # TODO 引入QStatusBar # 和上面搭配<01>

    def onMyToolBarButtonClick(self, s):
        print("click 点击", s)
        if s:
            label = QLabel("改变1")
            label.setAlignment(Qt.AlignBottom)  # 这个窗口使用什么对齐
            self.setCentralWidget(label)



        else:
            label = QLabel("This is a PyQt5 window!")

        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

