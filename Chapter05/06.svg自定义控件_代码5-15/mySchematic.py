from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter,QPen,QFont
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtCore import QRectF,QRect,Qt

class myQSchematic(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        # 预先加载背景图片
        self.svg_render_background = QSvgRenderer('images/dashboard.svg')
        self.svg_render_pointer = QSvgRenderer('images/pointer.svg')
        # 定义原理图中的变量
        self.__angle = -68  # 指针转动角度：-68-68度
        self.__percentage = 0 # 油量百分比：0-100

    @property # 对外属性，油量百分比：0-100
    def percentage(self):
        return self.__percentage
    @percentage.setter
    def percentage(self, value):
        if value !=self.__percentage:
            self.__percentage=value
            self.__angle = self.__percentage * 1.36 - 68 # 0-100速度对应-68-68度
            self.repaint()

    def paintEvent(self, event):
        painter =QPainter(self)
        pen = QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        # 01下面拖动窗口时，保证图形比例不变化，实现自适应
        ratio = 3/2 # 宽高比保持
        side= min(self.width()/ratio,self.height())
        painter.setViewport(QRect((int(self.width()-side*ratio)//2),
                                  int((self.height()-side)//2),
                                  int(side*ratio),
                                  int(side)))
        # 02设置窗口尺寸，实现绘图隔离
        windowRect = QRectF(0,0,600,400) # 这里的长宽也最好设置成同一比例3:2
        painter.setWindow(windowRect.toRect())
        # 03绘制矢量背景图片
        self.svg_render_background.render(painter,windowRect)
        # 04绘制矢量指针图片
        painter.save()
        painter.translate(300,278) # 旋转中心的位置为原点
        painter.rotate(self.__angle) # 指针顺时针旋转的角度-68*68°
        pointer_RectF = QRectF(-25,-115,50,140) #限制箭头长宽
        self.svg_render_pointer.render(painter,pointer_RectF)
        # painter.drawLine(0,0,0,100) # Y轴辅助
        # painter.drawLine(0,0,50, 0) # X轴辅助
        # 05下面工作绘制文字
        painter.restore()
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        painter.setFont(font)
        tag_pos = QRectF(0,268,600,25) # QRectF和居中对齐保证文字永远居中
        pen.setWidth(2)
        pen.setColor(Qt.GlobalColor.white)
        painter.setPen(pen)
        painter.setOpacity(1)
        painter.drawText(tag_pos, Qt.AlignmentFlag.AlignCenter, '%.0f' % self.__percentage)

if __name__ == "__main__":
    import sys
    from PyQt6 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    ui = myQSchematic()
    ui.setWindowTitle("SVG自定义背景示例")
    ui.show()
    sys.exit(app.exec())