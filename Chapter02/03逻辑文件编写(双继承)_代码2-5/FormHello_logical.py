from PyQt6.QtWidgets import QWidget,QApplication
from FormHello_ui import Ui_FormHello

class QmyWidget(QWidget, Ui_FormHello):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 下面放置业务代码
        self.btnStr = "多继承示例"
        self.btnHelloWorld.setText(self.btnStr)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormHello = QmyWidget()
    myFormHello.show()
    sys.exit(app.exec())
