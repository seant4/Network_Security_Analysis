from scapy.all import *
from pcap_handler import *


print("Capturing packets")
capture = sniff(count=5)
wrpcap("net6.pcap", capture)
pcap_file = "net6.pcap"
f = open("out.csv", "w+")
output_file = 'out.csv'


count = 0
first_timestamp = 0
line_list = []
f.writelines("Source, Destination, Time, Size, Proto, Sport, Port \n")

# Looping through all the packets in the PCAP
for (pkt_data, pkt_metadata,) in RawPcapReader(pcap_file):
    ether_pkt = Ether(pkt_data)
    ip_pkt = ether_pkt[IP]
    src = ip_pkt.src # Get the source IP
    dst = ip_pkt.dst # Get the destination IP
    
    # Calculate the relative timestamp of packets compared to the first packet
    timestamp = pkt_metadata.sec + (pkt_metadata.usec)/1000000
    if count == 0:
        first_timestamp = timestamp
        relative_timestamp = 0.0
    else:
        relative_timestamp = timestamp - first_timestamp
    
    pkt_size = pkt_metadata.caplen # Get packet size
    count += 1
    line = src + "," + dst + "," + str(round(relative_timestamp, 6)) + "," + str(pkt_size) + "," + str(ip_pkt.proto) + "," + str(ip_pkt.sport) + "," + str(ip_pkt.dport) + "\n"
    line_list.append(line)
    
f.writelines(line_list)
f.close()
    
