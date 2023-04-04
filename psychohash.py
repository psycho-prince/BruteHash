import hashlib
import os
import platform
import subprocess

# Install termcolor if not already installed
try:
    import termcolor
except ImportError:
    print("termcolor package not found. Installing...")
    if platform.system() == 'Linux':
        subprocess.call(['sudo', 'apt-get', 'update'])
        subprocess.call(['sudo', 'apt-get', 'install', 'python3-termcolor'])
    elif platform.system() == 'Darwin':
        subprocess.call(['pip3', 'install', 'termcolor'])
    else:
        subprocess.call(['pip', 'install', 'termcolor'])

from termcolor import colored
from art import *

ascii_banner = text2art('PSYCHO CRACKER')
print(colored(ascii_banner, 'blue'))

print("HASH CRACKER: ", end=" ")
tprint("PSYCHO")

print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384")

hash_type = input("What's your HASH type? ")
wordlist_location = input("Enter wordlist location: ")
hashed = input("Enter HASH: ")

word_list = open(wordlist_location, "r", encoding='utf-8', errors='ignore').read().splitlines()

for word in word_list:
    if hash_type == "MD5":
        hash_object = hashlib.md5(word.encode('utf-8'))
        hashed_word = hash_object.hexdigest()
        
    elif hash_type == "SHA1":
        hash_object = hashlib.sha1(word.encode('utf-8'))
        hashed_word = hash_object.hexdigest()
        
    elif hash_type == "SHA224":
        hash_object = hashlib.sha224(word.encode('utf-8'))
        hashed_word = hash_object.hexdigest()
        
    elif hash_type == "SHA512":
        hash_object = hashlib.sha512(word.encode('utf-8'))
        hashed_word = hash_object.hexdigest()
        
    elif hash_type == "SHA384":
        hash_object = hashlib.sha384(word.encode('utf-8'))
        hashed_word = hash_object.hexdigest()
    
    if hashed_word == hashed:
        print(colored("HASH FOUND: {}\n".format(word), 'green'))
        break
else:
    print(colored("HASH NOT FOUND", 'red'))
