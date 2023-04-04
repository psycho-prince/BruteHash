import hashlib
import subprocess

try:
    import art
except ImportError:
    print("Art module not found. Installing...")
    subprocess.check_call(['pip', 'install', 'art'])
    import art

ascii_banner = art.text2art('PSYCHO CRACKER')
print(ascii_banner)

print("HASHES CRACKER: ")
art.tprint("PSYCHO")

print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384")

hash_type = str(input("What's your HASH type? "))
wordlist_location = str(input("Enter wordlist location: "))
hashed = str(input("Enter HASH: "))

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
        print("\033[1;34;47mHASH FOUND: {}\n".format(word))
