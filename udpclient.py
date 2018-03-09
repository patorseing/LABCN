#!/usr/bin/python


import socket
import time

HOST = 'localhost'
PORT = 8000

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = raw_input('Input: ')
    if 'exit' in data:
        break
    else:
        s.sendto(data.encode(), (HOST, PORT))
        t = time.localtime()
        print('... connected from:', socket.gethostbyname('localhost'))
        print time.asctime(t)
        data, address = s.recvfrom(1024)
        print('received: %s' % data)
s.close()
