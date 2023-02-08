import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connecting client to server
s.connect((socket.gethostname(),1212))

#when we using socket.SOCK_STREAM , so we should identify size of bytes we want to recieve
msg = s.recv(1024)
print(msg.decode("utf-8"))
