import socket
import select
import errno
import sys

# import errno if number of client is more than we can handle
HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to ip-import
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    message = input(f'{my_username} > ')
   

    if message:
        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:

        while True:
            # recieve things from the client
            username_header = client_socket.recv(HEADER_LENGTH)
            # if we dont get any data for what ever reason
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit(0)

            username_length = int(username_header.decode('utf-8'))
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
            print('reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('Generel error', str(e))
        sys.exit()
