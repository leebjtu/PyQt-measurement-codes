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
from PyQt6.QtCore import Qt

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
        space = 4
        dashes = [1, space, 3, space, 9, space, 27, space, 9, space]
        pen.setDashPattern(dashes)

        pen.setWidth(2)
        pen.setColor(Qt.GlobalColor.black)
        painter.setPen(pen)
        # 3.开始绘图
        painter.drawLine(50, 50, 350, 200)
        painter.drawRect(200, 20, 60, 80)
        # painter.drawText(100, 250, "欢迎来到大武汉！")

if __name__=="__main__":
    app= QApplication(sys.argv)
    demo = QmyWidget()
    demo.show()
    sys.exit(app.exec())