#!/usr/bin/python

BUF_SZ = 32

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8080))
print s.recv(32)
