import hashlib
import pyfiglet
from art import *
import os
import getpass

ascii_banner = pyfiglet.figlet_format('PSYCHO CRACKER')
print(ascii_banner)

print("HASHES CRACKER: ", end=" ")
tprint("PSYCHO")

print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384")

hash_type = input("What's your HASH type? ")
wordlist_location = input("Enter wordlist location: ")
hashed = getpass.getpass("Enter HASH: ")

word_list = []
with open(os.path.join(wordlist_location), "r", encoding='utf-8', errors='ignore') as f:
    word_list = f.read().splitlines()

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
        print("\033[1;34;47mHASH FOUND: {}\n".format(word))