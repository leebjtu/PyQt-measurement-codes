from PyQt6.QtWidgets import QWidget,QApplication
from FormHello_ui import Ui_FormHello
from PyQt6.QtCore import QEvent

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_FormHello()
        self.ui.setupUi(self)
        # 下面放置业务代码
        self.btnStr = "示例按钮"
        self.ui.btnHelloWorld.setText(self.btnStr)
        self.ui.btnHelloWorld.resize(200,100)
        self.ui.btnHelloWorld.setMouseTracking(True)
        # 第01步：给需要响应事件的控件安装事件过滤器
        self.ui.btnHelloWorld.installEventFilter(self)
    # 第02步：父控件的统一处理所有子控件的事件响应
    def eventFilter(self, watched, event):
        if watched is self.ui.btnHelloWorld:
            if event.type() == QEvent.Type.MouseButtonDblClick:
                self.do_btnHelloWorld_MouseButtonDblClick(event)
            elif event.type() == QEvent.Type.MouseButtonPress:
                self.do_btnHelloWorld_MouseButtonPress(event)
            elif event.type() == QEvent.Type.Enter:
                self.do_btnHelloWorld_Enter(event)
            elif event.type() == QEvent.Type.Leave:
                self.do_btnHelloWorld_Leave(event)
            # 仅setMouseTracking(True)才触发
            elif event.type() == QEvent.Type.MouseMove:
                self.do_btnHelloWorld_MouseMove(event)
        # 如果还有其他控件事件，可以继续在下面列出，判断并处理
        # if watched == self.ui.xx:
        return super().eventFilter(watched, event)
    # 第03步：新定义控件的响应函数
    def do_btnHelloWorld_MouseButtonDblClick(self, event):
        self.ui.btnHelloWorld.setText("双击了按钮")

    def do_btnHelloWorld_MouseButtonPress(self, event):
        self.ui.btnHelloWorld.setText("单击了按钮")

    def do_btnHelloWorld_Enter(self, event):
        self.ui.btnHelloWorld.setText("鼠标进入")

    def do_btnHelloWorld_Leave(self, event):
        self.ui.btnHelloWorld.setText("鼠标移出")

    def do_btnHelloWorld_MouseMove(self, event):
        self.ui.btnHelloWorld.setText("(%d,%d)" % (event.pos().x(),event.pos().y()))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormHello = QmyWidget()
    myFormHello.show()
    sys.exit(app.exec())
