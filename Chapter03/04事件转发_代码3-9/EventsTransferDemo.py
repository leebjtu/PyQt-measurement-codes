from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtCore import Qt
# 底层的标签控件
class QmyLabel(QLabel):
    def mousePressEvent(self, ev : QMouseEvent):
        print("单击了标签！")
# 中间窗体控件
class QmyMiddleWidget(QWidget):
    def mousePressEvent(self, ev : QMouseEvent):
        print("单击了中间窗口！")
# 顶层窗体
class QmyTopWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 300)
        self.setWindowTitle("事件转发")
        # 中间窗体
        self.middeWidget = QmyMiddleWidget(self)
        self.middeWidget.move(50, 50)
        self.middeWidget.resize(250, 150)
        self.middeWidget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.middeWidget.setStyleSheet("border: 2px solid;")
        # 底层标签
        self.myLabel = QmyLabel(self.middeWidget)
        self.myLabel.move(50, 10)
        self.myLabel.resize(120, 20)
        self.middeWidget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.myLabel.setStyleSheet("border: 2px solid red;")
        self.myLabel.setText("我是标签")
    # 鼠标点击事件：点击鼠标时触发
    def mousePressEvent(self, mouseEvent :QMouseEvent):
        print("单击了顶层窗口！")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormEvent = QmyTopWidget()
    myFormEvent.show()
    sys.exit(app.exec())
