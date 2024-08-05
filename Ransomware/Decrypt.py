# pip install cryptography
import os
from cryptography.fernet import Fernet


file_Names = []

# Reading the all files on directory except program files
for file in os.listdir():
	if file in ["Encrypt.py", "Decrypt.py", "SecretKey.key"]:
		continue

	if os.path.isfile(file):
		file_Names.append(file)


# Reading the secret key from the key file
with open("SecretKey.key","rb") as secret_Key_File:
	secret_Key = secret_Key_File.read()


# Decrypt the data in each file
for file in file_Names:
	
	# Store the content of the file
	with open(file,"rb") as decrypt_File:
		contents = decrypt_File.read()
	
	# Apply decryption to data using the key
	contents_Decrypted = Fernet(secret_Key).decrypt(contents)

	# Writing decrypted data to orginal file
	with open(file,"wb") as decrypt_File:
		decrypt_File.write(contents_Decrypted)

		
		print("[+] The ", file , "is decrypted")
		print(contents_Decrypted, "\n\n")


