from scapy.all import *
from pcap_handler import *
import pandas as pd
import threading
import os
import time

PATH = ""
print("Capturing packets")

def convert_capture(capture):
    source = []
    destination = []
    sport = []
    dport = []
    for i in capture:
        if (IP in i) and (TCP in i):
            if IPv6 not in i:
                source.append(i[IP].src)
                destination.append(i[IP].dst)
                sport.append(i[TCP].sport)
                dport.append(i[TCP].dport)
    data = {'Source': source, 'Destination': destination, "Source Port": sport, "Destination Port": dport}
    df = pd.DataFrame(data)
    df.to_csv("table.csv")

cap = rdpcap(PATH) #Pull from file
#cap = sniff(count=10)
convert_capture(cap)