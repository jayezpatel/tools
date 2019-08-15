#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear',shell=True)

remote_server = raw_input("Enter the IP or Hostname to scan: ")
server_ip = socket.gethostbyname(remote_server)
l_port = raw_input("From range: ")
h_port = raw_input("To range: ")
starttime=datetime.now()

try:
    for port in range(int(l_port),int(h_port)+1):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((server_ip,port))
        if (result == 0):
            print "Port",port,"is open."
        sock.close()

except KeyboardInterrupt:
    print "\nYou pressed ctrl + c. Exiting Now.\n"
    sys.exit()

except socket.gaierror:
    print "\nHostname could not be resolved.\n"
    sys.exit()

except socket.error:
    print "\nCould not connect to socket.\n"
    sys.exit()

endtime=datetime.now()

totaltime=endtime-starttime

print "Total time to scan : ", totaltime
