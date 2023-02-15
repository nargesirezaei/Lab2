import socket
# this gives us os-level I/O capabilities
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server doesn’t connect to a client. Instead it sets itself up on a specific address and port.
# This is done with a call to bind. Like connect, this function takes a tuple containing an address and a port.
# The operating system will try to reserve the address/port combination for our server application.
# server_socket.bind((IP,PORT))

# One common issue is that the OS often will not recycle which ports are considered used.
# So if we stop and start our server a lot, it may not be able to reserve the same port again.
#  To fix this, we can tell the socket to reuse its address if needed. This is done with the following code
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

# now we should manage a list of clients, or client_socket.
server_socket.listen()
sockets_list = [server_socket]

# Thinks like raport clients to other clients. client is dictionary, where the client-socket will be the key
# and then the user data will be teh value


clients = {}

print(f'Listening for connections on {IP}:{PORT}...')
# main server job = recieve messages


def recieve_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        # if we didnt get any data, client close the connection
        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False


while True:
    # select.select takes 3 parameters, 1=> read_list(the thing u wanna read. 2=> [] that means the socket
    # that gonna write. 3=> socket that actually is the one that we want to read and get data from)
    read_socket, _, exception_sockets = select.select(
        sockets_list, [], sockets_list)

    for notified_socket in read_socket:
        # thats mean someone just connected and we should accept this connection and handle it
        if notified_socket == server_socket:
            # so:
            clien_socket, client_address = server_socket.accept()

            user = recieve_message(clien_socket)
            if user is False:
                continue
            # otherwise: append client_socket to that list we made
            sockets_list.append(clien_socket)
            # we got user, a dictionary od data
            clients[clien_socket] = user
            print(
                f"accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
            # if someone just connected, but otherwise:
        else:
            # recieve message from client
            message = recieve_message(notified_socket)
            if message is False:
                print(
                    f"close connection from: {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(
                f"recieved message from {user['data'].decode('utf-8')}:{message['data'].decode('utf-8')}")

            # for the purpose of not sending the msg client send back to the same client:

            for client_socket in clients:
                if client_socket != notified_socket:
                    # both username with header info and message with its header and information
                    client_socket.send(
                        user['header'] + user['data'] + message['header'] + message['data'])

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]
