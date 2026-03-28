from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPainter, QMouseEvent, QKeyEvent, QPaintEvent
from PyQt6.QtCore import QPointF, Qt
class QmyLabel(QLabel):
    def mouseDoubleClickEvent(self, ev : QMouseEvent):
        self.setText("双击了标签！")

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(300, 200)
        self.mylabel = QmyLabel(self)
        self.mylabel.move(50, 10)
        self.mylabel.resize(120,20)
        self.mylabel.setStyleSheet("background-color:yellow;")
        self.mylabel.setText("按钮")
    # 窗体重绘事件：界面重绘时触发
    def paintEvent(self, event:QPaintEvent):
        painter = QPainter(self)
        painter.drawEllipse(QPointF(self.height()/3, self.height()/3), self.height()/4,  self.height()/4)
        super().paintEvent(event)
    # 键盘按键事件：按下键盘时触发
    def keyPressEvent(self, keyEvent: QKeyEvent):
        key = keyEvent.key()
        keyName = Qt.Key(key).name
        self.mylabel.setText("按键按下：%s" % keyName)
        super().keyPressEvent(keyEvent)
    # 鼠标点击事件：点击鼠标时触发
    def mousePressEvent(self, mouseEvent :QMouseEvent):
        msPoint = mouseEvent.pos()
        if mouseEvent.button() == Qt.MouseButton.LeftButton:
            self.mylabel.setText("鼠标按下：(%d,%d)"%(msPoint.x(),msPoint.y()))
        super().mousePressEvent(mouseEvent)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormEvent = QmyWidget()
    myFormEvent.show()
    sys.exit(app.exec())
