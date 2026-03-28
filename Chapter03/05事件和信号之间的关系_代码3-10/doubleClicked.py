from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6.QtCore import pyqtSignal

class QmyButton(QPushButton):
    doubleClicked = pyqtSignal()
    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(300, 200)
        self.myButton = QmyButton(self)
        self.myButton.move(120, 100)
        self.myButton.setText("双击我")
        self.myButton.doubleClicked.connect(self.do_myButton_doubleClicked)

    # 自定义槽函数
    def do_myButton_doubleClicked(self):
        print("双击了按钮")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormHello = QmyWidget()
    myFormHello.show()
    sys.exit(app.exec())
