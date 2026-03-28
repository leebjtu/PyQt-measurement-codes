## demo_Helloworld.py
import sys
from PyQt6 import QtWidgets

# 01.这里放置定义的窗口逻辑
app = QtWidgets.QApplication(sys.argv)  # 使用QApplication创建app
# 02.这里放置定义的窗口逻辑
widgetHello = QtWidgets.QWidget()  # 创建窗体
widgetHello.resize(400, 300)    # 设置窗体宽高
widgetHello.setWindowTitle("Demo Hello world!")  # 设置窗体标题

btnHello = QtWidgets.QPushButton(widgetHello)  # 在窗体上添加按钮
btnHello.setText("hello world!")  # 按钮上添加文字
btnHello.setGeometry(150, 120, 100, 30)  # 设置按钮的位置和长宽

widgetHello.show()  # 显示对话框
# 03.开启线程循环
sys.exit(app.exec())
