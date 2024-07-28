import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
	scapy_packet = scapy.IP(packet )