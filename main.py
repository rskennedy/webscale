#!/usr/bin/python

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = socket.gethostname()
sk.bind((host_ip, 8080))
sk.listen(5)

while True:
    (client_sk, addr) = sk.accept()
    print "recieved client", addr
    client_sk.send("Successfully connected!")
    client_sk.close()
