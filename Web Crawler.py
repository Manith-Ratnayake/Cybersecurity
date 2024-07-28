import requests
import urllib.parse as urlparse
import re



def requests(url):
	try:
		return requests.get("https://" + url)

	except requests.exceptions.ConnectionError:
		pass



def subdomains():
	with open("/root/Downloads/common.txt", "r") as wordlist_file:
		for line in wordlist_file:
			word = line.strip()
			test_url = target_url + "/" + word
			response = requests(test_url)

		if response:
			print("[+] Discovered url --> " + test_url)



def extract_link_form(url):
	response = requests.get(target_url)
	return re.findall("", str(response.content.decode(errors="ignore")))



def crawl():
	href_links = extract_link_form(url)

	for link in href_links:
		link = urlparse.urljoin(url, link)
		
		if "#" in link:
			link = link.split("#")[0]

		if target_url in link and link not in target_links:
			target_links.append(link)
			print(link)
			crawl(link)



target_links = []
target_url = ""

crawl(target_url)