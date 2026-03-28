#!/usr/bin/env python3
# coding=utf-8
"""
Author: 三石
Time: 2022-01-13
File: main.py
Function: QPainter的使用示例.
"""
import sys
from PyQt6.QtWidgets import QApplication,QWidget
from PyQt6.QtGui import QPainter, QPen, QBrush
from PyQt6.QtCore import Qt

class QmyWidget(QWidget):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.setWindowTitle("使用QPainter绘图示例") # 设置标题
        self.resize(400,300) # 设置窗口大小

    def paintEvent(self, event):
        painter = QPainter(self)
        # 1.绘图和文字抗锯齿
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)
        # 2.设置笔
        pen = QPen()
        pen.setColor(Qt.GlobalColor.black)
        painter.setPen(pen)
        # 3.设置笔刷
        brush = QBrush()
        brush.setColor(Qt.GlobalColor.red)
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        # 4.开始绘图
        painter.drawLine(10, 10, 350, 200)
        painter.drawRect(200, 20, 60, 80)
        painter.drawText(100, 250, "欢迎来到大武汉！")

if __name__=="__main__":
    app= QApplication(sys.argv)
    demo = QmyWidget()
    demo.show()
    sys.exit(app.exec())