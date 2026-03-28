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
from PyQt6.QtGui import QPainter, QPen, QPainterPath,QColor
from PyQt6.QtCore import Qt, QRect, QPoint

class QmyWidget(QWidget):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.setWindowTitle("使用QPainterPath绘图示例") # 设置标题
        self.resize(400,300) # 设置窗口大小

    def paintEvent(self, event):
        painter = QPainter(self)
        # 1.绘图和文字抗锯齿
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)
        # 2.设置笔
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(Qt.GlobalColor.black)
        painter.setPen(pen)
        # 3.获取物理设备宽高度
        W = self.width() # 绘图设备物理宽度：400像素
        H = self.height() # 图设备物理高度：300像素
        # 4.标记一块矩形区域作为视口
        physicalRect = QRect(0,0,W,H)
        painter.setViewport(physicalRect)
        # 5.创建一块矩形区域作为窗口
        windowRect = QRect(0,0,800,600)
        painter.setWindow(windowRect) # 建立映射
        # 6.在逻辑坐标系上，即窗口视图上绘图QPainterPath
        pathLogo  = QPainterPath()
        pathLogo.addRect(50, 50, 200, 200)
        pathLogo.moveTo(0, 0)
        pathLogo.cubicTo(300, 0,  150, 150,  300, 300)
        pathLogo.cubicTo(0, 300,  150, 150,  0, 0)
        pathLogo.setFillRule(Qt.FillRule.OddEvenFill) # 默认：OddEvenFill，WindingFill
        painter.setBrush(QColor(122, 163, 39))
        painter.drawPath(pathLogo)
        painter.drawText(120,150,"logo1")

        painter.save()
        painter.translate(500,50)
        painter.rotate(45)
        painter.drawPath(pathLogo)
        painter.drawText(120, 150, "logo2")
        painter.restore()


if __name__=="__main__":
    app= QApplication(sys.argv)
    demo = QmyWidget()
    demo.show()
    sys.exit(app.exec())