import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.220.81', 8080))
# 接收小于 1024 字节的数据
print("waiting for message:\n")
msg = s.recv(1024)
print("message is:%s" % msg.decode('utf-8'))
s.send(msg)
s.close()