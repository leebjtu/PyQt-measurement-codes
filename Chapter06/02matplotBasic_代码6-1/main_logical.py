# main_logical.py
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets
from main_ui import Ui_Form
from PyQt6.QtCore import QTimer, pyqtSlot
import numpy as np
class mainLogical(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timeInterval = 500 # ms
        self.timer.setInterval(self.timeInterval)
        self.timer.timeout.connect(self.timerOut)
        self.t = 0 # 时间
        self.ui.myWaveform.addChannel(legend='channel0', fmt='r-')
        self.ui.myWaveform.addChannel(legend='channel1', fmt='g--')
    # 定时器溢出槽函数
    def timerOut(self):
        self.t += self.timeInterval/1000
        x= np.linspace(self.t,self.t+self.timeInterval/1000,100)
        f = 5 # Hz
        y1 = np.sin(2*np.pi*f*x)
        y2 = 2*np.cos(2*np.pi*f*x)
        self.ui.myWaveform.getChannel(0).addXYArrays(x,y1)
        self.ui.myWaveform.getChannel(1).addXYArrays(x,y2)
    # 点击开始按钮槽函数
    @pyqtSlot()
    def on_btnStart_clicked(self):
        if self.ui.btnStart.text()== '开始':
            self.timer.start()
            self.ui.btnStart.setText('停止')
        else:
            self.timer.stop()
            self.ui.btnStart.setText('开始')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mainLogical()
    ui.show()
    sys.exit(app.exec())
