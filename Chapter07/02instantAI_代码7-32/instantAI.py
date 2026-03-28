from Chapter07.PyAdvantech import InstantAiCtrl, BioFailed, DeviceInformation
from System import Array, Double
import time
# 调用.net程序集中的DeviceCtrl对象的函数
deviceDescription = "DemoDevice,BID#0"
profilePath = "../profile/DemoDevice.xml"
channelCount = 2
startChannel = 0
def AdvInstantAI():
    # 01.创建InstantAiCtrl对象，选择设备，并初始化
    instanceAiObj = InstantAiCtrl()
    instanceAiObj.SelectedDevice = DeviceInformation(deviceDescription)
    ret = instanceAiObj.LoadProfile(profilePath)
    if BioFailed(ret):
        print("loadProfile失败了！error_code:%x" % ret)
    # 02.读取指定通道数据
    while True:
        scaledData = Array[Double](range(0, channelCount))
        ret = instanceAiObj.Read(startChannel, channelCount, scaledData)
        if BioFailed(ret):
            print("instantAiCtrl 失败了！error_code:%x" % ret)
            instanceAiObj.Dispose() # 结束释放资源
            break
        else:
            print("%d个通道数据：\n%s "%(channelCount, str(list(scaledData))))
            time.sleep(1)


if __name__ == '__main__':
    AdvInstantAI()