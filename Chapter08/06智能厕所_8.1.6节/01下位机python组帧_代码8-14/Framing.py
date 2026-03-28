import serial
import struct
def generateFrame(format_str, *args):
    # 按格式字符串的生成结构体变量
    data_struct = struct.Struct(format_str)
    # 生成放数据的缓冲区
    data_bytes = bytearray(data_struct.size)
    # 写入缓冲区数据，生成字节流
    data_struct.pack_into(data_bytes, 0, *args)  # 写入缓冲区数据，生成字节流
    # 填充校验码
    data_bytes[-1] = sum(data_bytes[:-1]) & 0xFF # 校验和取结果低8位
    print(data_bytes.hex('-'))
    return data_bytes
# 程序入口
if __name__ == '__main__':
    # 01.准备数据
    frame_header = b'\x55\xaa'  # 帧头
    operater = 0x01  # 操作码
    length = 14  # 帧数据长度
    temperature = 12.34  # 温度
    humidity = 45.67  # 湿度
    headCount = 10  # 人头数
    stall0 = 1  # 蹲位1
    stall1 = 1  # 蹲位1
    stall2 = 0  # 蹲位0
    stall3 = 0  # 蹲位0
    stall4 = 1  # 蹲位1
    stalls = stall4 << 4 | \
             stall3 << 3 | \
             stall2 << 2 | \
             stall1 << 1 | \
             stall0
    checksum = 0x00
    # 02.打包数据
    data_bytes = generateFrame('<2s2B2fi2B', frame_header,
                                 headCount,
                               stalls,
                               checksum)
    # 03.发送数据
    with serial.Serial("com3", 9600) as ser:
        ser.write(data_bytes)