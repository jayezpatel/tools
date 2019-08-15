import os
import sys
import ipaddress

netw = sys.argv[1]
hostname = ipaddress.ip_network(unicode(netw))
#print "Scanning network ",hostname.network

for ip in hostname.hosts():
    response = os.system("ping -c 1 > /dev/null 2>&1 "+unicode(ip))
    if response == 0:
        print ip, 'is up!'
    else:
        print ip, 'is down!'
