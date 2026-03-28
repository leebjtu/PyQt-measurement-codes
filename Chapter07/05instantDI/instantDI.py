from Chapter07.PyAdvantech import InstantDiCtrl, BioFailed, DeviceInformation
from System import Array, Byte
import time
# 调用.net程序集中的DeviceCtrl对象的函数
deviceDescription = "DemoDevice,BID#0"
profilePath = "../profile/DemoDevice.xml"
start_port = 0
port_count = 2
def AdvBufferedAI():
    # 01.创建InstantAoCtrl对象，选择设备
    InstantDiCtrlObj = InstantDiCtrl()
    InstantDiCtrlObj.SelectedDevice = DeviceInformation(deviceDescription)
    try:
        # 02.加载配置文件
        ret = InstantDiCtrlObj.LoadProfile(profilePath)
        if BioFailed(ret):
            raise Exception("loadProfile失败了！error_code:%x" % ret)
        # 03.读数据
        while True:
            # 读具体的指定port的所有值
            data = Array[Byte](range(0, port_count))
            ret = InstantDiCtrlObj.Read(start_port, port_count, data)
            if BioFailed(ret):
                raise Exception("InstantDi读取port数据失败了！error_code:%x" % ret)
            else:
                print("%d个通道数据：\n%s " % (port_count, str(list(data))))
            # 读具体的指定port的指定bit位
            ret, data_byte = InstantDiCtrlObj.ReadBit(0, 1, 0) # port=0， bit=1,最后一个参数忽略
            if BioFailed(ret):
                raise Exception("InstantDi读取bit数据失败了！error_code:%x" % ret)
            else:
                print("data_byte:%d"%data_byte)
            time.sleep(0.5)
    finally:
        InstantDiCtrlObj.Dispose()
if __name__ == '__main__':
    AdvBufferedAI()

