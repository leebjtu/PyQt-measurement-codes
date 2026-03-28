from PyQt6.QtWidgets import QWidget,QApplication,QRadioButton
from UDFSlot_ui import Ui_FormSlot
class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_FormSlot()
        self.ui.setupUi(self)
    # 下面放置业务代码
        self.ui.rbtnBanana.clicked.connect(self.do_groupBox_clicked)
        self.ui.rbtnOrange.clicked.connect(self.do_groupBox_clicked)
        self.ui.rbtnWatermelon.clicked.connect(self.do_groupBox_clicked)
    # 自定义槽函数
    def do_groupBox_clicked(self):
        for rbtn in (self.ui.rbtnOrange,
                      self.ui.rbtnBanana,
                      self.ui.rbtnWatermelon):
                if rbtn.isChecked() == True:
                    self.ui.lineEdit.setText(rbtn.text())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormHello = QmyWidget()
    myFormHello.show()
    sys.exit(app.exec())
