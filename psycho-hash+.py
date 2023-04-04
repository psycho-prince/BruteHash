import os
import sys

# check if pip is installed, if not install it
try:
    import pip
except ImportError:
    os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
    os.system('python get-pip.py')
    os.remove('get-pip.py')
    
# check if pip3 is installed, if not install it
try:
    import pip3
except ImportError:
    os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
    os.system('python3 get-pip.py')
    os.remove('get-pip.py')

# install required packages
try:
    import termcolor
except ImportError:
    os.system('pip install termcolor')

try:
    from art import *
except ImportError:
    os.system('pip install art')

# import required modules
import hashlib
from termcolor import colored
from art import text2art

# print banner
banner_text = "HASH CRACKER"
print(colored(text2art(banner_text, font='block'), 'green'))

# get user input
hash_type = input("Enter hash type (md5, sha1, sha256, sha384, sha512): ")
wordlist_location = input("Enter wordlist location: ")
hashed = input("Enter hash: ")

# read wordlist file
try:
    with open(wordlist_location, 'r', encoding='utf-8', errors='ignore') as f:
        word_list = f.read().splitlines()
except FileNotFoundError:
    print(colored("Error: Wordlist file not found", 'red'))
    sys.exit()

# iterate through wordlist and check for matching hash
for word in word_list:
    if hash_type == "md5":
        hashed_word = hashlib.md5(word.encode('utf-8')).hexdigest()
    elif hash_type == "sha1":
        hashed_word = hashlib.sha1(word.encode('utf-8')).hexdigest()
    elif hash_type == "sha256":
        hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()
    elif hash_type == "sha384":
        hashed_word = hashlib.sha384(word.encode('utf-8')).hexdigest()
    elif hash_type == "sha512":
        hashed_word = hashlib.sha512(word.encode('utf-8')).hexdigest()
    else:
        print(colored("Error: Invalid hash type", 'red'))
        sys.exit()
        
    if hashed_word == hashed:
        print(colored("Hash found: " + word, 'green'))
        sys.exit()

print(colored("Hash not found in wordlist", 'red'))
