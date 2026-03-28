'''
本程序先安装pythonnet包
用来测试使用pythonnet是否成功调用dll
如果调用成功，则会打印出当前安装的所有采集卡描述
'''
from Chapter07.PyAdvantech import DeviceCtrl

# 调用.net程序集中的DeviceCtrl对象的函数
def getInstalledDevices():
    installed_device_descriptions = []
    installed_devices = DeviceCtrl.InstalledDevices
    for installed_device in installed_devices:
        installed_device_descriptions.append(installed_device.Description)
    return installed_device_descriptions  # 返回所有安装了的板卡的描述符，是个list类型
# 打印已安装的硬件
print(getInstalledDevices())
