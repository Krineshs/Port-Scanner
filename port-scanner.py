import socket

Address = 0

Address = input('Please input the Local Ip Adress you would like to scan: ')
startport = input('Please input the Port you would like to START scanning from: ')
endport = input('Please input the Port you would like to END scanning from: ')

x = int(startport)
y = int(endport)+1

for port in range(x, y):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((Address, port))
    if result == 0:
        print("Port " + str(port) + " is open")
    else:
        print("Port " + str(port) + " is closed")
    sock.close()
