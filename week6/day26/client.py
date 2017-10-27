# @Time    : 2017/10/27 0027 16:24
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : client.py

import socket

sk =socket.socket()
print(sk)
address = ('127.0.0.1',8000)
sk.connect(address)

# data = sk.recv(1024) #阻塞
data = sk.send(bytes('hah','utf8'))
print(str(data,'utf8'))
sk.close()