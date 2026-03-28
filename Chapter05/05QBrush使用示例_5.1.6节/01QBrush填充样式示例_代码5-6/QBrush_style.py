#!/usr/bin/env python3
# coding=utf-8
"""
Author: 三石
Time: 2022-01-13
File: QBrush_style.py
Function: QBrush的填充样式示例
"""
import sys
from PyQt6.QtWidgets import QApplication,QWidget
from PyQt6.QtGui import QPainter, QPen, QBrush, QPixmap
from PyQt6.QtCore import Qt, QRectF, QPointF

class QmyWidget(QWidget):
    BRUSH_STYLE_LIST = [Qt.BrushStyle.NoBrush,
                        Qt.BrushStyle.SolidPattern,
                        Qt.BrushStyle.Dense7Pattern,
                        Qt.BrushStyle.HorPattern,
                        Qt.BrushStyle.VerPattern,
                        Qt.BrushStyle.CrossPattern,
                        Qt.BrushStyle.BDiagPattern,
                        Qt.BrushStyle.FDiagPattern,
                        Qt.BrushStyle.DiagCrossPattern]

    def __init__(self, parent =None):
        super().__init__(parent)
        self.setWindowTitle("使用QBrush的填充效果示例") # 设置标题
        self.resize(800,600) # 设置窗口大小

    def paintEvent(self, event):
        painter = QPainter(self)
        # 1.绘图和文字抗锯齿
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)
        # 2.设置笔
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(Qt.GlobalColor.black)
        # pen.setColor(QColor(200,100,3))
        painter.setPen(pen)
        # 3.获取物理设备宽高度
        W = self.width() # 绘图设备物理宽度：400像素
        H = self.height() # 图设备物理高度：300像素
        # 4.绘制不同填充的矩形
        brush = QBrush()
        for i in range(len(QmyWidget.BRUSH_STYLE_LIST)):
            brush.setStyle(QmyWidget.BRUSH_STYLE_LIST[i])
            brush.setColor(Qt.GlobalColor.red)
            painter.setBrush(brush)
            painter.drawRect(QRectF(W/20+(i%3)*W/3, H/10 +(i//3)*W/5, W/8, 2*H/10))
            painter.drawText(QPointF(W/20+(i%3)*W/3, 7*H/20+(i//3)*W/5), str(QmyWidget.BRUSH_STYLE_LIST[i]) )


        # brush = QBrush()
        # texturePixmap = QPixmap("img.png")
        # brush = QBrush()
        # # brush.setStyle(Qt.BrushStyle.TexturePattern) # 此句话可以不加了
        # brush.setTexture(texturePixmap)
        # painter.setBrush(brush)
        # painter.drawRect(QRectF(W/10, H/10, 4*W/5, 4*H/5))

if __name__=="__main__":
    app= QApplication(sys.argv)
    demo = QmyWidget()
    demo.show()
    sys.exit(app.exec())