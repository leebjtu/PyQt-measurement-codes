from Chapter07.PyAdvantech import BufferedAoCtrl, BioFailed, DeviceInformation
from System import Array, Double
import math
# 调用.net程序集中的DeviceCtrl对象的函数
deviceDescription = "DemoDevice,BID#0"
profilePath = "../profile/pci1712.xml"
channelStart = 0
channelCount = 2
# 波形缓冲区的变量数据
frequency = 50  # Hz,周期波形的频率
oneWavePointCount = 100  # 每个周期波形的点数
waveCounts = 50  # sample中一共多少个周期的波形
sampleCount = waveCounts * oneWavePointCount  # sample的总点数
intervalCount = sampleCount // 4  # 每个通道中sample中section的个数
# 单个通道的采样频率，不是内部时钟的频率，范围为152.59-1M/channelcount(500K) 注意，转化频率共享DAC的触发
convertClkRate = oneWavePointCount * frequency
# 波形类别
class WAVESTYLE(object):
    SINE = 0  # 正弦波
    SAWTOOTH = 1  # 锯齿波
    SQUARE = 2  # 方波
    CUSTOM = 3  # 自定义
def bufferedAoCtrl_DataTransmitted(sender, e):
    print("sender.ConvertClock.Rate:%.2f" % (intervalCount / sender.ConvertClock.Rate))
    print('来自DataTransmitted事件: 已经发送的点数为: %d' % e.Count)
def bufferedAoCtrl_TransitStopped(sender, e):
    print('来自TransitStopped事件')
def bufferedAoCtrl_Underrun(sender, e):
    print('来自Underrun事件: 空缺的点数为: %d' % e.Count)
def bufferedAoCtrl_Stopped(sender, e):
    print("来自Stopped事件")
# 融合一个周期多个通道内的波形数据点
def generateWaveform(channelCount, oneWavePointCount, waveStyle):
    oneWaveSamplesCount = oneWavePointCount
    mergedData = [0.0] * oneWavePointCount * channelCount
    for channel_index in range(0, channelCount):
        data_list = createOneWaveData(oneWaveSamplesCount, waveStyle)
        for data_index in range(0, oneWaveSamplesCount):  # 融合多通道数据到一个mergedData中
            mergedData[channel_index + data_index * channelCount] = data_list[data_index]
    return mergedData
# 产生一个通道内的的波形数据
def createOneWaveData(oneWavePointCount, waveStyle):
    waveData = [0.0] * oneWavePointCount
    max_voltage = 4
    min_voltage = 1
    for point_index in range(0, oneWavePointCount):
        if waveStyle == WAVESTYLE.SINE:
            amplitude = (max_voltage - min_voltage) / 2  # 峰峰值
            offset = (max_voltage + min_voltage) / 2  # 偏置
            waveData[point_index] = amplitude * math.sin(point_index * 2.0 * math.pi / oneWavePointCount) + offset
        elif waveStyle == WAVESTYLE.SQUARE:
            pass
        elif waveStyle == WAVESTYLE.SAWTOOTH:
            pass
        elif waveStyle == WAVESTYLE.CUSTOM:
            pass
    return waveData
# 主程序
def AdvBufferedAO():
    # 01.创建InstantAoCtrl对象，选择设备
    waveformAoObj = BufferedAoCtrl()
    waveformAoObj.SelectedDevice = DeviceInformation(deviceDescription)
    waveformAoObj.DataTransmitted += bufferedAoCtrl_DataTransmitted
    waveformAoObj.TransitStopped += bufferedAoCtrl_TransitStopped
    waveformAoObj.Underrun += bufferedAoCtrl_Underrun
    waveformAoObj.Stopped += bufferedAoCtrl_Stopped
    waveformAoObj.Streaming = True  # specify the running mode: streaming-buffered.
    try:
        # Step 02: 加载配置文件，如果采用第03步手动配置，此步可以删除
        ret = waveformAoObj.LoadProfile(profilePath)
        if BioFailed(ret):
            raise Exception("loadProfile失败了！error_code:%x" % ret)
        # Step 03: 手动配置AO参数
        waveformAoObj.ScanChannel.ChannelStart = channelStart
        waveformAoObj.ScanChannel.ChannelCount = channelCount
        waveformAoObj.ScanChannel.IntervalCount = intervalCount
        waveformAoObj.ScanChannel.Samples = sampleCount
        waveformAoObj.ConvertClock.Rate = convertClkRate
        # Step 04：准备数据
        errorCode = waveformAoObj.Prepare()
        if BioFailed(errorCode):
            raise Exception("prepare出错！")
        # Step 05：生成周期波形数据
        userBufferList = generateWaveform(channelCount, oneWavePointCount, WAVESTYLE.SINE) * waveCounts
        scaledWaveData = Array[Double](userBufferList)
        waveformAoObj.SetData(scaledWaveData.Length, scaledWaveData)
        # Step 05：开始采集
        errorCode = waveformAoObj.Start()
        if BioFailed(errorCode):
            raise Exception("Start出错！")
        # Step 7: 这里阻塞，可以替换成你想要做的任何事情
        input(' StreamingAI is in progress... any key to quit !')
    finally:
        waveformAoObj.Dispose()
if __name__ == '__main__':
    AdvBufferedAO()

