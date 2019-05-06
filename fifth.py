import socket
import time


my_socket = socket.socket()
my_socket.connect(('35.157.111.68', 10042))
my_socket.recv(1024)
g = "g"
while not g == "":
    print("waiting")
    info = my_socket.recv(1024)
    print(info)
    g = ""
    for i in str(info):
        if i.isnumeric():
            g += i

    my_socket.send(g.encode())
    print(g)
    time.sleep(1)
