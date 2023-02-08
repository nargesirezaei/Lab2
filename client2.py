import socket
headersixe = 10
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1235))



while True:

    full_msg = ''
    new_msg = True
    while True:
     msg = s.recv(16)
     if new_msg:
        print(f"new msg length: {msg[:headersixe]}")
        msglen = int (msg[:headersixe])
        new_msg = False
    
     full_msg += msg.decode("utf-8")
     if len(full_msg)-headersixe == msglen:
        print("full msg recieved ")
        print(full_msg[headersixe:])
        new_msg = True
        full_msg = ''

        print(full_msg)