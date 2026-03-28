#!/usr/bin/env python3
# coding=utf-8
"""
Author: 三石
Time: 2022-01-13
File: main.py
Function: QPainter的使用示例.
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QPoint

class QmyWidget(QWidget):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.setWindowTitle("使用QPen CustomDashLine绘图示例") # 设置标题
        self.resize(400,300) # 设置窗口大小


    def paintEvent(self, event):
        painter = QPainter(self)
        # 1.绘图和文字抗锯齿
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)
        # 2.设置笔
        pen = QPen()
        pen.setWidth(30)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        # pen.setJoinStyle(Qt.PenJoinStyle.BevelJoin)
        # pen.setJoinStyle(Qt.PenJoinStyle.MiterJoin)
        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        pen.setColor(Qt.GlobalColor.black)
        painter.setPen(pen)
        # 3.开始绘图
        painter.drawPolyline(QPoint(50, 50),
                             QPoint(350, 150),
                             QPoint(50, 250))

if __name__=="__main__":
    app= QApplication(sys.argv)
    demo = QmyWidget()
    demo.show()
    sys.exit(app.exec())