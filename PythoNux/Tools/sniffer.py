from scapy.all import *

def imprimi_pacote(packet):
	header = str(packet[TCP].payload[0:4])
	if header == 'POST':
		if 'pass' in str(packet[TCP].payload).lower()
		print(packet.show())

sniff(filter='', store=0, prn=imprimi_pacote)


