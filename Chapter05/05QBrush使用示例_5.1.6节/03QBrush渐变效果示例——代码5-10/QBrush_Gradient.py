#!/usr/bin/env python3
# coding=utf-8
"""
Author: 三石
Time: 2022-07-13
File: QBrush_Gradient.py
Function: QBrush的渐变填充样式示例
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QGradient, QLinearGradient, QRadialGradient, QConicalGradient
from PyQt6.QtCore import Qt, QRectF, QPointF


class QmyWidget(QWidget):
    GRADIENT_SPREAD = [QGradient.Spread.PadSpread,
                       QGradient.Spread.RepeatSpread,
                       QGradient.Spread.ReflectSpread]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("使用QBrush的渐变效果示例")  # 设置标题
        self.resize(800, 600)  # 设置窗口大小

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
        W = self.width()  # 绘图设备物理宽度：400像素
        H = self.height()  # 图设备物理高度：300像素
        # 4.绘制不同填充的矩形
        for i in range(3):
            rect = QRectF(W / 20 + (i % 3) * W / 3, H / 10 + (i // 3) * W / 5, W / 8, 2 * H / 10)
            start_point = QPointF(rect.left(), (rect.top() + rect.bottom()) * 1 / 3)
            end_point = QPointF(rect.left(), (rect.top() + rect.bottom()) * 2 / 3)


            linear_gradient = QLinearGradient(start_point, end_point)
            linear_gradient.setColorAt(0, Qt.GlobalColor.white)
            linear_gradient.setColorAt(1, Qt.GlobalColor.red)
            linear_gradient.setSpread(QmyWidget.GRADIENT_SPREAD[i])
            painter.setBrush(linear_gradient)
            painter.drawRect(rect)
            painter.drawText(QPointF(W / 20 + (i % 3) * W / 3, 7 * H / 20),
                             str(QmyWidget.GRADIENT_SPREAD[i]))

            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawEllipse(start_point, 2, 2)  # 绘制其实标记点
            painter.drawEllipse(end_point, 2, 2)

            # 4.绘制不同填充的矩形
        for i in range(3):
            circle_center = QPointF(W / 8 + (i % 3) * W / 3, H/2)
            R = W / 12

            fx = circle_center.x()
            fy = circle_center.y()
            conical_gradient = QRadialGradient(circle_center.x(), circle_center.y(), R/5, fx, fy)
            conical_gradient.setColorAt(0, Qt.GlobalColor.white)
            conical_gradient.setColorAt(1, Qt.GlobalColor.red)
            conical_gradient.setSpread(QmyWidget.GRADIENT_SPREAD[i])
            painter.setBrush(conical_gradient)
            painter.drawEllipse(circle_center, R, R)
            painter.drawText(QPointF(W / 20 + (i % 3) * W / 3, 13 * H / 20),
                             str(QmyWidget.GRADIENT_SPREAD[i]))

            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawEllipse(circle_center, 2, 2)
            painter.drawEllipse(QPointF(circle_center.x()+R/5, circle_center.y()), 2, 2)



        for i in range(3):
            circle_center = QPointF(W / 8 + (i % 3) * W / 3, H * 4/ 5)
            R = W / 12
            conical_gradient = QConicalGradient(circle_center, 45)
            conical_gradient.setColorAt(0, Qt.GlobalColor.white)
            conical_gradient.setColorAt(1, Qt.GlobalColor.red)
            conical_gradient.setSpread(QmyWidget.GRADIENT_SPREAD[i])
            painter.setBrush(conical_gradient)
            painter.drawEllipse(circle_center, R, R)
            painter.drawText(QPointF(W / 20 + (i % 3) * W / 3, 19 * H / 20),
                             str(QmyWidget.GRADIENT_SPREAD[i]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QmyWidget()
    demo.show()
    sys.exit(app.exec())
