# !/usr/bin/python
"""
Simple tcp client that will connect to given port/ip combo.

Created by Riley Kennedy on 5/18/2018

"""
import socket
import sys
from time import sleep

""" Helper Functions """


def uerror(message):
    print "ERROR: ", message
    exit(1)


def isIPv4(ip_addr):
    ip_octets = list(ip_addr.split('.'))
    if len(ip_octets) != 4: return False
    for octet in ip_octets:
        try:
            oct_val = int(octet)
        except ValueError:
            return False
        if not 0 <= oct_val < 256: return False
    return True


BUF_SIZE = 128
address = ""

if len(sys.argv) < 2:
    print "The client expects an ip/port combination in this format --> 10.0.0.0:22"
    address = raw_input("Please input a valid target ip and port: ")
else:
    address = sys.argv[1]

try:
    (ip, port_string) = address.split(':')
    port = int(port_string)
except ValueError:
    uerror("Invalid format for ip/port combination")

if isIPv4(ip) == False:
    uerror("Invalid format for ip")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
print "Successful connection to ", ip

s.settimeout(3)
response = ""
try:
    response = s.recv(BUF_SIZE)
    print "response from server: ", response
except socket.timeout:
    print "No reply received."
s.close()
