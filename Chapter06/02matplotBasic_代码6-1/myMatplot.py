# myMatplot.py
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSizePolicy, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
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

class myChannel():
    # axes：当前曲线所在子图；
    # legend：当前曲线的图例
    # fmt：曲线描述符，'r--x'
    # kwargs：曲线属性描述键值对
    def __init__(self, axes, legend, fmt, **kwargs):
        self.line = axes.plot([], [], fmt, **kwargs)[0]  # 注意返回是一个list，只取list[0]
        self.line.set_label(legend)  # 赋值给图例
        self.axes = axes
        self.axes.legend() # 图例生效
        self.axes.legend().set_draggable(True)
        self.canvas = self.axes.figure.canvas
    # 为当前通道赋予数据,添加数据后，更新画布
    def addXYArrays(self, XdataArray, YdataArray):
        self.line.set_data(XdataArray, YdataArray)
        self.axes.set_xlim(XdataArray[0], XdataArray[-1])
        self.canvas.draw() # 更新画布

if __name__ == "__main__":
    from PyQt6 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myQMatplot()
    MainWindow.show()
    MainWindow.addChannel(legend='legend232', fmt='r-x')
    MainWindow.getChannel(0).addXYArrays([0,1,2,3,4,5],[1.2,2.2,3.5,2.5,1,1.5])

    sys.exit(app.exec())




