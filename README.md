# Network Packet Analysis

Packet visualization tool for ports and IP addresses on IPv4

## Description

This project visualizes the movement of packets through ports and their corresponding IP addresses via IPv4. As described in *Network Security Through Data Analysis: Building Situational Awareness*, 
> Imagine a network is a two-dimensional grid, where the x axis shows your IP addresses and the y-axis shows the ports. The grid will then have k cells, where k is the total number of IP addresses. ... As a rule of thumb, defenders scan vertially and attackers horizontally

cap_convert.py takes in a .cap file and converts it to a suitable csv for the packet_analysis.R to visualize. 

## Getting Started

### Dependencies

* Scapy - Handles packet manipulation
* Pcap-handler - For .pcap support
* Pandas - Data manipulation
* ggplot2 - Visualization
### Executing program

* cap_conver.py
1. For .cap support, edit the path vairable
```
PATH = 'path/to/.cap'
```
2. Live analysis is also avilable
```
cap = sniff(count = n) #n = number of packets
```

* packet_analysis.R
1. Provide table.csv pah
```
PATH = path/to/table.csv
```

## Authors

* Sean Theisen

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License

## Acknowledgments

Inspiration, code snippets, etc.
* [Network Security Through Data Analysis](https://www.oreilly.com/library/view/network-security-through/9781449357894/index.html)
