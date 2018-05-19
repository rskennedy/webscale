"""
Created by Riley Kennedy

Simple port scanner.
Given a target IP address, the scanner will discover which ports are open.
It should be noted probing each possible port can take some time, and open
ports are printed to console after the scan has completed.

Last updated: 5/18/2018 by Riley Kennedy

"""

"""
Potential Features:
* Allow for user to specify subnets rather than one IP.
* Reformat this as an importable module. 
"""

import socket
import sys
import logging.handlers
from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call  # Execute a shell command
from datetime import datetime as time

""" Helper Functions """


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Ping command count option as function of OS
    param = '-n 1' if system_name().lower() == 'windows' else '-c 1'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, host]

    # Pinging
    return system_call(command) == 0


""" Main logic """

CONN_REFUSED = 111
PORT_RANGE_START = 0
PORT_RANGE_STOP = 2 ** 16
target_ip = ""
open_ports = []
logger = logging.getLogger()
logging.basicConfig(filename="logs/pscan.log", level=logging.DEBUG)

if len(sys.argv) < 2:
    target_ip = raw_input("Please input a target ip: ")
else:
    target_ip = sys.argv[1]

# Checks if host is reachable
# TODO: suppress output from ping system call
print "Pinging target ip..."
print ""
reachable = ping(target_ip)
if reachable == False:
    print "Failed to reach target ip"
    print "exiting..."
    sys.exit(1)
else:
    print "target reachable"

logger.info("\n\n\n Data from %s", time.now())
for port in xrange(PORT_RANGE_START, PORT_RANGE_STOP):
    if port == 135: continue
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn_status = s.connect_ex((target_ip, port))
    if conn_status == CONN_REFUSED:
        logger.info(" connection refused on port %d", port)
        continue
    open_ports.append(port)
    s.close()

print "Found %d open ports on %s:" % (len(open_ports), target_ip)
for port in open_ports: print port
