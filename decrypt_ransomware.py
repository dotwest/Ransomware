#!/usr/bin/env python3

import os
import subprocess
from colorama import Fore, Style
import time
from cryptography.fernet import Fernet

time.sleep(1)

#creating empty list of file to append when list listing file 

files = []

#the loop will checks if any files are if it finds any files it will decrypt it

for file in os.listdir():

#this step will escape the file from non_encrypted file 

	if file == "decrypt_ransomware.py" or file == "thekey.key" or file == "secret.txt":
		continue

#appending the files it found

	if os.path.isfile(file): 
		files.append(file)

print(Fore.BLUE+"[#]Your files to be decrypted:\n")

print(files)

print(Style.RESET_ALL)

""" in this steps it will check the key file and read the contents and prompt to user to enter the secret key and start to decrypt"""

with open("thekey.key", "rb") as thekey:
	secretkey = thekey.read()

user = input("Enter the secret key in secret.txt to decrypt files: ")

""" this steps will continue when the correct key word is entered and it open encrypted fil3s and read the contents and after that it decryt the read contents and write  decrypt contents of the repective file  """

if user == "decrypt_me":
	for file in files:
		with open(file, "rb") as theread:
			contents = theread.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thewrite:
			thewrite.write(contents_decrypted)
	print(Fore.GREEN+"[#]All files are decrypted safely and successfully"+Style.RESET_ALL)
else:
	print(Fore.RED+"[#]YOU HAVE ENTERED A WRONG DECRYPTION CODE!, Files are still encrypted"+Style.RESET_ALL)

