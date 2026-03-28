from PyQt6.QtWidgets import QWidget,QApplication
from UDFSlot_ui import Ui_FormSlot
from PyQt6.QtCore import pyqtSlot
class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_FormSlot()
        self.ui.setupUi(self)
    # 下面放置业务代码
        self.ui.btnAdd.setCheckable(True)

    @pyqtSlot(bool)
    def on_btnAdd_clicked(self, checked):
        self.ui.lcdCounts.display(self.ui.lcdCounts.value()+1)
        print('on_btnTest_clicked is :'+str(checked))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormHello = QmyWidget()
    myFormHello.show()
    sys.exit(app.exec())
