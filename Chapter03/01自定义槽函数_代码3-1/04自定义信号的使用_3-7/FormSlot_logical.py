from PyQt6.QtWidgets import QWidget,QApplication
from FormSender_ui import Ui_FormSender
from FormReceiver_ui import Ui_FormReceiver
from PyQt6.QtCore import pyqtSignal, pyqtSlot
class QmySenderWidget(QWidget):
    # 定义自定义overload型信号
    dataSendSig = pyqtSignal([str], [int], [float])
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_FormSender()
        self.ui.setupUi(self)
    # 下面放置业务代码
    @pyqtSlot()
    def on_btnSendText_clicked(self):
        text = self.ui.lineEdit.text()
        self.dataSendSig[str].emit(text)

    @pyqtSlot()
    def on_btnSendInt_clicked(self):
        intNum = self.ui.spinBox.value()
        self.dataSendSig[int].emit(intNum)

    @pyqtSlot()
    def on_btnSendFloat_clicked(self):
        doubleNum = self.ui.doubleSpinBox.value()
        self.dataSendSig[float].emit(doubleNum)

class QmyReceiverWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_FormReceiver()
        self.ui.setupUi(self)
        self.senderWidget = QmySenderWidget()
        # 自定义信号连接
        self.senderWidget.dataSendSig[str].connect(self.do_dataReceived_str)
        self.senderWidget.dataSendSig[int].connect(self.do_dataReceived_int)
        self.senderWidget.dataSendSig[float].connect(self.do_dataReceived_float)
    @pyqtSlot()
    def on_btnOpenChild_clicked(self):
        self.senderWidget.show()
    # 自定义槽函数
    def do_dataReceived_str(self, str: str):
        self.ui.txtEditReceiver.setText("收到文本："+str+'\n')
    def do_dataReceived_int(self, intNum: int):
        self.ui.txtEditReceiver.setText("收到整形："+str(intNum)+'\n')
    def do_dataReceived_float(self, floatNum: float):
        self.ui.txtEditReceiver.setText("收到浮点数："+str(floatNum)+'\n')
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myFormHello = QmyReceiverWidget()
    myFormHello.show()
    sys.exit(app.exec())
