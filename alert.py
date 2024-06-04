from scapy.all import *
from pcap_handler import *
import pandas as pd
import threading

print("Capturing packets")
flag = False

def interrupt():
    global flag
    input("Press any key to stop\n")
    flag = True

def main_capture():
    source = []
    destination = []
    sport = []
    dport = []
    interrupt_thread = threading.Thread(target=interrupt)
    interrupt_thread.start()
    while(flag == False):
        capture = sniff(count=10)

        for i in capture:
            if (IP in i) and (TCP in i):
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

main_capture()
