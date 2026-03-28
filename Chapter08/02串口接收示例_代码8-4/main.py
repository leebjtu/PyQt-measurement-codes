import serial
# 请确定设备管理器有串口设备,如果没有,可以装一个虚拟串口调试
if __name__ == '__main__':
    ser = serial.Serial("com1", 9600, timeout=1)

 # 查询方法：
    while True:
        data = ser.read(10)  # 阻塞，读到10字节，或者超时1s后返回
        if len(data) != 0:
            print("收到数据如下：\n"+data.decode('utf-8'))
        else:
            print("读超时且缓冲区为空")