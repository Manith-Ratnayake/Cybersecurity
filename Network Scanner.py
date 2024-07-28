import scapy.all as scapy


def scan():
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast / arp_request
	answerd_list = scapy.srp(arp_request_broadcast, timeout = 2, verbose = False)[0]

	client_list = []
	for element in answerd_list:
		client_dict = {"ip":element[1].psrc , "mac":element[1].hwsrc}
		client_list.append(client_dict)

	return client_list



def print_results(results_dict):
	print("IP\t\tMAC Address")
	for client in client_list:
		print(client["ip"] + "\t\t" + client["mac"])



def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t","--target", dest="target", help="Target IP address" )
	options = parser.parse_args()
	return options



options = get_arguments()
scan_results = scan(options.target)
print(scan_results)