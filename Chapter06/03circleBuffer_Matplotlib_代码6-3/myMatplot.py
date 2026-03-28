# myMatplot.py
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSizePolicy, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
class myQMatplot(QWidget):
    def __init__(self, parent =None, width=8, height=5):
        super().__init__(parent)
        # 01.下面是为了正常显示中文标签
        plt.rcParams["font.sans-serif"] = ['SimHei','KaiTi'] # 汉字字体
        plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号
        plt.rcParams["font.size"] = 9  # 字号
        # 02.在画布上绘制Figure对象
        self.fig = Figure(figsize=(width, height)) # 单位：英寸
        self.figCanvas = FigureCanvas(self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # 03.加上工具栏
        self.toolbar = NavigationToolbar(self.figCanvas, self, coordinates=True)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        # 04.增加子图，默认只有1个绘图
        self.ax = self.fig.add_subplot(111) # 也可以用add_axes()
        # 05.设置ax轴标签信息
        self.initAxes()
        # 06.布局
        self.initLayout()
        # 07.数据
        self.channels = []  # 存放所有的通道数据
    # 初始化子图标签信息
    def initAxes(self):
        # https://matplotlib.org/stable/api/axes_api.html
        self.ax.set_title('电压-时间曲线')
        self.ax.set_xlabel('时间/s')
        self.ax.set_ylabel('电压/V')
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(-5, 5)
        self.ax.grid(axis='both')
    # 布局
    def initLayout(self):
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.figCanvas)
    # 增加通道
    def addChannel(self, legend='legend', fmt='-', **kwargs):
        channel = myChannel(self.ax, legend, fmt, **kwargs)
        self.channels.append(channel)
    # 获取当前通道
    def getChannel(self, index):
        return self.channels[index]

#*************环形缓冲区初始化**************
class myChannel():
    def __init__(self, axes, legend, fmt, **kwargs):
        self.__axes = axes
        self.__max_chunks = 10 # 缓冲区的个数
        self.__lines = [] # 存放缓冲区对象line2D的列表
        self.__buffer_index = 0 # 缓冲区指针
        self.__last_data_x = None
        self.__last_data_y = None
        self.__x_span = 2  # 默认X轴的宽度为5s
        self.__x_span_offset = 0  # 默认X轴的右边空个几秒
        self.initCircleBuffer(legend, fmt, **kwargs)
    # 初始化环形缓冲区，把通道的图例等属性赋值给第0个line
    def initCircleBuffer(self, legend, fmt, **kwargs):
        for index in range(0,self.__max_chunks):
            line = self.__axes.plot([], [], fmt, **kwargs)[0]  # 注意返回是一个list，只取list[0]
            if index == 0:  # 只有第一个加上图例
                line.set_label(legend)
                self.__axes.legend()
            self.__lines.append(line)  # 增加max_chunks个curve给curves
    # 向通道添加数据，入口数据类型为np.ndarray
    def addXYArrays(self, x_array, y_array):
        # 01如果到最后一个缓冲区，则从第0个重新开始
        if self.__buffer_index >= len(self.__lines):
            self.__buffer_index = 0
        # 02每个line之间头尾数据连不上线，故后来的line头数据多画一个点（前一个line尾点）
        x_array = np.insert(x_array, 0, self.__last_data_x)
        y_array = np.insert(y_array, 0, self.__last_data_y)
        self.__last_data_x = x_array[-1]
        self.__last_data_y = y_array[-1]
        # 03赋值最新数据给当前缓冲区
        self.__lines[self.__buffer_index].set_data(x_array, y_array)
        # 04设置x轴的标签范围
        self.__axes.set_xlim(x_array[-1] - self.__x_span + self.__x_span_offset, x_array[-1] + self.__x_span_offset)
        self.__axes.figure.canvas.draw()  # 更新画布
        self.__buffer_index += 1

if __name__ == "__main__":
    from PyQt6 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myQMatplot()
    MainWindow.show()
    MainWindow.addChannel(legend='legend232', fmt='r-x')
    MainWindow.getChannel(0).addXYArrays([0,1,2,3,4,5],[1.2,2.2,3.5,2.5,1,1.5])

    sys.exit(app.exec())




