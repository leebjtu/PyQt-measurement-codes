#!/usr/bin/python3
# 文件名：tcpServer.py

import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.220.81"
port = 9999
serversocket.bind((host, port))
serversocket.listen(10)
print("开始监听：")
while True:
    clientsocket, addr = serversocket.accept()
    print("连接地址: %s" % str(addr))
    msg = clientsocket.recv(1024)
    print("来自客户端的消息："+msg.decode("utf-8"))
    clientsocket.send(msg)
    clientsocket.close()