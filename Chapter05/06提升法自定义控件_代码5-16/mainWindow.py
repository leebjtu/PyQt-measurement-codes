#!/usr/bin/env python3
# coding=utf-8
"""
Author: 三石
Time: 2022-01-08
File: mainWindow.py
Function: QmyTank使用示例的业务逻辑类.
"""
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget
from mainWindow_ui import Ui_MainWindow
from PyQt6.QtCore import pyqtSlot

class QmyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("提升法自定义控件demo")
        self.ui.sliderValue.setRange(self.ui.spinMinValue.value(), self.ui.spinMaxValue.value())
        self.ui.myTank.liquidLevelChanged.connect(self.do_level_changed)
# ===========QmyTank中定义的信号关联的自定义槽函数================
    def do_level_changed(self, value):
        self.ui.labelValue.setText(str(value))

# ===========connectSLotByName()自动关联槽函数==============
    def on_sliderValue_valueChanged(self,value):
        self.ui.myTank.value = value

    @pyqtSlot(float)
    def on_spinMinValue_valueChanged(self, value): # value是获取spinMinValue的浮点数据
        self.ui.myTank.minValue = value

    @pyqtSlot(float)
    def on_spinMaxValue_valueChanged(self, value): # value是获取spinMaxValue的浮点数据
        self.ui.myTank.maxValue = value

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec())
