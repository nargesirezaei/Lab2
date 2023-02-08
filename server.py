import socket;
##lager en socket for client og setter vi til to parameter som utgjør typen av socket-en
# socket.AF_INET => indicates that underlying network is using IPv4
#socket.SOCK_STREAM => indicates that it is a TCP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding server socket til et spesific port som server bruker til å ta i mot requset fra client
s.bind((socket.gethostname(),1234))

#server will preapre a queue of 5
s.listen(5)


while True:
    #alle klineter som har med hostname og addresse, dvs. IP og portnummer skal få koble seg med server
    clientsocket, address = s.accept()
     
    #once we got that connenction, printing out this msg
    print(f"connection from {address} has been stablished! ")
    
    #then send we this msg to client-socket
    clientsocket.send(bytes("welcome to the server","utf-8"))
    clientsocket.close()
    




