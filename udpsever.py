#!/usr/bin/python

import socket

HOST = 'localhost'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    print('Waiting for connection . . . ')
    data, address = s.recvfrom(1024)
    print('... connected from:', str(address))
    if data:
        print('received: %s' % data)
        s.sendto(data.upper(), address)
s.close()
