import socket
import time
headersixe = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1235))

s.listen(5)


#that telling us about the size of msg we will recieve from server
while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been stablished! ")


    msg = "welcome to server!"
    msg = f"{len(msg):<{headersixe}}" + msg
    
    clientsocket.send(bytes(msg,"utf-8"))
    #and now we dont need to close it 
    clientsocket.close()



    #this code showing the time after 3 seconds
    while True:
        time.sleep(3)

        msg = f"the time is: {time.time()}"
        msg = f"{len(msg):<{headersixe}}" + msg
        clientsocket.send(bytes(msg, "utf-8"))

    

