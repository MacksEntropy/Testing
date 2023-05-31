# import socket, time
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('localhost', 80))
# while True:
#     time.sleep(5)
#     data = client_socket.recv(512)
#     if data.lower() == 'q':
#         client_socket.close()
#         break

#     print("RECEIVED: %s" % data)
#     data = input("SEND( TYPE q or Q to Quit):")
#     client_socket.send(data)
#     if data.lower() == 'q':
#         client_socket.close()
#         break

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print buf
        break