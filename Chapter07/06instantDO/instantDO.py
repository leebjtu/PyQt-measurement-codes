from Chapter07.PyAdvantech import InstantDoCtrl, BioFailed, DeviceInformation
import time
from System import Array, Byte

# 调用.net程序集中的DeviceCtrl对象的函数
deviceDescription = "PCI-1712,BID#0"
profilePath = "../profile/DemoDevice.xml"
start_port = 0
port_count = 2
def AdvBufferedAI():
    # 01.创建InstantAoCtrl对象，选择设备
    InstantDoCtrlObj = InstantDoCtrl()
    InstantDoCtrlObj.SelectedDevice = DeviceInformation(deviceDescription)
    try:
        # 02.加载配置文件
        ret = InstantDoCtrlObj.LoadProfile(profilePath)
        if BioFailed(ret):
            raise Exception("loadProfile失败了！error_code:%x" % ret)
        # 03.写数据
        write_data = Array[Byte]([0x00, 0x00])
        ret = InstantDoCtrlObj.Write(start_port, port_count, write_data)
        if BioFailed(ret):
            raise Exception("InstantDo写port失败了！error_code:%x" % ret)
        time.sleep(1)
        # 写指定port指定bit位数据
        ret = InstantDoCtrlObj.WriteBit(0, 0, 1)
        if BioFailed(ret):
            raise Exception("InstantDo写bit失败了！error_code:%x" % ret)
        # 04.阻塞，直到按键被按下后结束
        input(' StreamingAI is in progress... any key to quit !')
    finally:
        InstantDoCtrlObj.Dispose()
if __name__ == '__main__':
    AdvBufferedAI()

