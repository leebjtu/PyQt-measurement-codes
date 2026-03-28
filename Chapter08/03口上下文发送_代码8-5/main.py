import serial
if __name__ == '__main__':
    # 上下文发送字符串：
    with serial.Serial("com3", 9600) as ser:
        ser.write(b'hello')