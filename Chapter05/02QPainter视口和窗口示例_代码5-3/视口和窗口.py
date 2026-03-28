#!/usr/bin/env python3
# coding=utf-8
"""
Author: 三石
Time: 2022-01-13
File: 视口和窗口.py
Function: QPainter的视口和窗口示例.
"""
import sys
from PyQt6.QtWidgets import QApplication,QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QRect, QPoint

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
        pen.setWidth(10)
        pen.setColor(Qt.GlobalColor.black)
        painter.setPen(pen)
        # 3.获取物理设备宽高度
        W = self.width() # 绘图设备物理宽度：400像素
        H = self.height() # 图设备物理高度：300像素
        # 4.标记一块矩形区域作为视口
        physicalRect = QRect(W//4, H//4, W*2//4, H*2//4) # (100, 75, 200, 150)
        # physicalRect = QRect(100, 75, 200, 150)
        painter.setViewport(physicalRect)
        # 5.创建一块矩形区域作为窗口
        windowRect = QRect(0,0,800,600)
        painter.setWindow(windowRect) # 建立映射
        # 6.在逻辑坐标系上，即窗口视图上绘图
        painter.drawRect(windowRect)
        painter.drawLine(0, 0, 800, 600)
        painter.drawEllipse(QPoint(0,0),20,20)

if __name__=="__main__":
    app= QApplication(sys.argv)
    demo = QmyWidget()
    demo.show()
    sys.exit(app.exec())