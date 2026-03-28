from Chapter07.PyAdvantech import WaveformAiCtrl, BioFailed, DeviceInformation
from System import Array, Double
import matplotlib.pyplot as plt
# 调用.net程序集中的DeviceCtrl对象的函数
deviceDescription = "DemoDevice,BID#0"
profilePath = "../profile/DemoDevice.xml"
def AdvBufferedAI():
    # 01.创建WaveformAiCtrl对象，选择设备，关联DataReady和Overrun事件
    WaveformAiObj = WaveformAiCtrl()
    WaveformAiObj.DataReady += waveformAiCtrl_dataReady
    WaveformAiObj.Overrun += waveformAiCtrl_overrun
    WaveformAiObj.SelectedDevice = DeviceInformation(deviceDescription)
    try:
        # 02.此步骤非必须，查看本采集设备是否支持buffered Ai模式
        bool_ret = WaveformAiObj.Features.BufferedAiSupported
        if not bool_ret:
            raise Exception("本卡不支持StreamAI模式！")
        # 03.加载配置文件
        ret = WaveformAiObj.LoadProfile(profilePath)
        if BioFailed(ret):
            raise Exception("loadProfile失败了！error_code:%x" % ret)

        WaveformAiObj.Conversion.ChannelStart = 0
        WaveformAiObj.Conversion.ChannelCount = 2
        WaveformAiObj.Conversion.ClockRate = 10000
        WaveformAiObj.Record.SectionLength = 5000
        WaveformAiObj.Record.SectionCount = 0

        # 04.Prepare()准备
        ret = WaveformAiObj.Prepare()
        if BioFailed(ret):
            raise Exception("Prepare失败了！error_code:%x" % ret)
        # 05.开始采集，填充缓冲区
        errorCode = WaveformAiObj.Start()
        if BioFailed(errorCode):
            raise Exception("Start！error_code:%x" % ret)
        # 06.阻塞，直到按键被按下后结束
        input(' StreamingAI is in progress... any key to quit !')
    finally:
        # 07.释放资源
        WaveformAiObj.Dispose()

def waveformAiCtrl_dataReady(sender, e):
    # if e.Count <= 0:
    #     print("No data available to read\n")
    #     return
    WaveformAiObj = sender
    # 获取对象中的一些设置数据
    conversion = WaveformAiObj.Conversion
    channel_count = conversion.ChannelCount
    start_channel = conversion.ChannelStart
    convert_clk_rate = conversion.ClockRate # Hz/Channel
    section_length = WaveformAiObj.Record.SectionLength
    # 推算一些变量值
    frame_time = section_length / convert_clk_rate  # 每次触发时间间隔
    convert_period = 1.0 / convert_clk_rate  # 采样周期：每个点采样间隔
    # 准备缓冲区
    section_buffer = Array[Double](range(0, section_length * channel_count))  # 取出来的原始数据
    # 静态变量声明
    if not hasattr(waveformAiCtrl_dataReady, "time_buffer"):
        waveformAiCtrl_dataReady.time_buffer = [i * convert_period for i in range(section_length)]
    waveformAiCtrl_dataReady.time_buffer = [(data + frame_time) for data in waveformAiCtrl_dataReady.time_buffer]

    WaveformAiObj.GetData(section_length * channel_count, section_buffer)

    list_section_buffer = list(section_buffer)
    plot_data(waveformAiCtrl_dataReady.time_buffer, list_section_buffer, channel_count)

def plot_data(dataX, dataY, channel_count):
    plt.ion()  #   mode 成功的关键函数
    if not hasattr(plot_data, "fig"):
        plot_data.fig = plt.figure(figsize=(16, 8))
        plot_data.ax0 = plot_data.fig.add_axes([0.1, 0.1, 0.4, 0.8])  # 在left, bottom, width, height = 0.1, 0.1, 0.8, 0.8

        plot_data.ax0.set_title('Data in channel0')
        plot_data.ax0.set_xlabel('Time/s')
        plot_data.ax0.set_ylabel('Voltage/V')

        plot_data.ax1 = plot_data.fig.add_axes([0.55, 0.1, 0.4, 0.8])  # 在图表的右下方创建一个子图
        plot_data.ax1.set_title('Data in channel1')
        plot_data.ax1.set_xlabel('Time/s')
        plot_data.ax1.set_ylabel('Voltage/V')
        plot_data.lines0, = plot_data.ax0.plot(dataX, dataY[0::channel_count])
        plot_data.lines1, = plot_data.ax1.plot(dataX, dataY[1::channel_count])
        plot_data.ax0.set_autoscaley_on(True)
        plot_data.ax1.set_autoscaley_on(True)


    plot_data.lines0.set_data(dataX, dataY[0::channel_count])
    plot_data.ax0.relim()
    plot_data.ax0.autoscale_view()

    plot_data.lines1.set_data(dataX, dataY[1::channel_count])
    plot_data.ax1.relim()
    plot_data.ax1.autoscale_view()

    plot_data.fig.canvas.draw()
    plot_data.fig.canvas.flush_events()

def waveformAiCtrl_overrun(sender, BfdAiEventArgs):
    print("Streaming AI is Over run !")
    print("缓冲区没来得及取的数据个数为：%d" % BfdAiEventArgs.Count)

if __name__ == '__main__':
    import matplotlib
    matplotlib.use('TkAgg')  # 显式设置后端
    AdvBufferedAI()