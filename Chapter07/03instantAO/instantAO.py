from Chapter07.PyAdvantech import InstantAoCtrl, BioFailed, DeviceInformation
from System import Array, Double
# 调用.net程序集中的DeviceCtrl对象的函数
deviceDescription = "DemoDevice,BID#0"
profilePath = "../profile/DemoDevice.xml"
startChannel = 0
channelCount = 2
def AdvBufferedAI():
    # 01.创建InstantAoCtrl对象，选择设备
    InstantAoCtrlObj = InstantAoCtrl()
    InstantAoCtrlObj.SelectedDevice = DeviceInformation(deviceDescription)
    try:
        # 02.加载配置文件
        ret = InstantAoCtrlObj.LoadProfile(profilePath)
        if BioFailed(ret):
            raise Exception("loadProfile失败了！error_code:%x" % ret)
        # 03.写数据
        write_data = [1, 2] # channel0=1V,channel1=2V
        scaledData = Array[Double](write_data)
        ret = InstantAoCtrlObj.Write(startChannel, channelCount, scaledData)
        if BioFailed(ret):
            raise Exception("Write失败了！error_code:%x" % ret)
        # 04.阻塞，直到按键被按下后结束
        input('InstantAO is in progress... any key to quit !')
    finally:
        InstantAoCtrlObj.Dispose()
if __name__ == '__main__':
    AdvBufferedAI()

