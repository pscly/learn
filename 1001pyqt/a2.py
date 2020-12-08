import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    w = QWidget()    
    layout = QHBoxLayout()      # 从左到右的布局
    btn = QPushButton("Hello World!")   # 创建一个按钮
    layout.addWidget(btn)   # 将按钮添加到布局中，布局会自动排列
    w.setLayout(layout)     # 将布局添加到窗口

    w.show()
    sys.exit(app.exec_())