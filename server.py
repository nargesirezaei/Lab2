import socket;
#defining our client-socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding, telling which local protocol liten to
s.bind((socket.gethostname(),1212))
s.listen(5)

while True:
    #connenct whatever connection from client
    #address is client ip address, and clientsocket is object
    clientsocket, address = s.accept()
    print(f"connection from {address} has been stablished! ")
    clientsocket.send(bytes("welcome to the server","utf-8"))
    clientsocket.close()
    




