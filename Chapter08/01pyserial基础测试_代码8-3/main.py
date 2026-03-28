import serial
if __name__ == '__main__':
    ser = serial.Serial("com3", 9600, timeout=1)
    ser.write(b'hello')
    ser.write('hello123'.encode('utf-8'))
    ser.readall()
    ser.close()
