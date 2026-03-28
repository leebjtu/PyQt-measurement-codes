from PyQt6.QtWidgets import QWidget,QApplication
from UDFSlot_ui import Ui_FormSlot
from PyQt6.QtCore import pyqtSlot
class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_FormSlot()
        self.ui.setupUi(self)
    # 下面放置业务代码
    def on_btnTest_pressed(self):
        self.ui.lcdCounts.display(self.ui.lcdCounts.value()+1)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormHello = QmyWidget()
    myFormHello.show()
    sys.exit(app.exec())
