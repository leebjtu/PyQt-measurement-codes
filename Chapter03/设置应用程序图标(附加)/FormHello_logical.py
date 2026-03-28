from PyQt6.QtWidgets import QWidget,QApplication
from PyQt6.QtGui import QIcon
from FormHello_ui import Ui_FormHello

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui=Ui_FormHello()
        self.__ui.setupUi(self)
        # 下面放置业务代码
        self.btnStr = "单继承示例"
        self.__ui.btnHelloWorld.setText(self.btnStr)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormHello = QmyWidget()
    icon = QIcon("Health.ico")
    myFormHello.setWindowIcon(icon)
    myFormHello.show()
    sys.exit(app.exec())
