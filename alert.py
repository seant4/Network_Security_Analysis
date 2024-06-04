from scapy.all import *
from pcap_handler import *
import pandas as pd

print("Capturing packets")
capture = sniff(count=10)
source = []
destination = []
sport = []
dport = []

for i in capture:
    if IP in i:
        if IPv6 not in i:
            source.append(i[IP].src)
            destination.append(i[IP].dst)
            sport.append(i[TCP].sport)
            dport.append(i[TCP].dport)


data = {'IP': destination, 'Port': dport}
df = pd.DataFrame(data)
fg = pd.pivot_table(df, index='Port', columns='IP', aggfunc='size', fill_value=0)
print(fg)
rs = fg.sum(axis=1).tolist()
print(rs)

