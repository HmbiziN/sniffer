from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        if packet[IP].dport == 80:
            print("\n{} => {}:{}".format(packet[IP].src, packet[IP].dst, packet[IP].dport), str(bytes(packet[TCP].payload)))

sniff(filter='tcp', prn=packet_callback, store=0, count=0)
