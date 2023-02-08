import socket
#lager en socket for client og setter vi til to parameter som utgjør typen av socket-en
# socket.AF_INET => indicates that underlying network is using IPv4
#socket.SOCK_STREAM => indicates that it is a TCP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#binder client socket to server med to parameteret. første er server hostname, og den andre er det portet som 
#server bruker til å ta i mot forespørsel fra client
#i den tilfelle både server og client er samme så host name blir også det samme
s.connect((socket.gethostname(),1234))


full_msg = ''
while True:
    msg = msg.rec(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
    print(full_msg)
