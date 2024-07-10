import requests
import traceback
import re

def webConnection(url):

	try:
		response = requests.get(url)

		with open("connection_results.txt","wb") as file:
			file.write(response.content)

		with open("hello.txt","rb") as file:
			file = file.readlines()
		
		return True

	except requests.exceptions.ConnectionError as e:
		print("[-] Connection Error occured  to >>", url)
		return False


def subDomains():

	target_url = "google.com"

	with open("Subdomain.txt","r") as file:

		for line in file:
			word = line.strip()
			web_url = "https://" + word + "." + target_url

			response = webconnection(web_url)

			if response:
				print("[+] Discovered Sub Domains " , web_url)




def hiddenPaths():

	target_url = "https://www.zsecurity.org"
	response = requests.get(target_url)
	response = str(response.content)

	c = '(?:href=")(.*?)"'

	href_link = re.findall(c, response)
	print(href_link)


hiddenPaths()