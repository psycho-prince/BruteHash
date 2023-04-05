import hashlib

def main():
    while True:
        print_ascii_cat("PSY 💀 HASH 💀 CRACKER 💀")
        print("1. Crack a hash\n2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            hash_to_crack = input("Enter the hash to crack: ")
            wordlist_path = input("Enter the path to the wordlist: ")
            encoding = input("Enter the character encoding of the wordlist (press Enter for default UTF-8): ") or "utf-8"
            
            print("Supported hash formats:")
            print("1. md5\n2. sha1\n3. sha224\n4. sha256\n5. sha384\n6. sha512")
            hash_format = input("Enter the number of the hash format to use: ")

            try:
                with open(wordlist_path, "r", encoding=encoding) as f:
                    for word in f:
                        word = word.strip()
                        if hash_format == "1":
                            hashed_word = hashlib.md5(word.encode(encoding)).hexdigest()
                        elif hash_format == "2":
                            hashed_word = hashlib.sha1(word.encode(encoding)).hexdigest()
                        elif hash_format == "3":
                            hashed_word = hashlib.sha224(word.encode(encoding)).hexdigest()
                        elif hash_format == "4":
                            hashed_word = hashlib.sha256(word.encode(encoding)).hexdigest()
                        elif hash_format == "5":
                            hashed_word = hashlib.sha384(word.encode(encoding)).hexdigest()
                        elif hash_format == "6":
                            hashed_word = hashlib.sha512(word.encode(encoding)).hexdigest()
                        else:
                            print("Invalid hash format.")
                            break
                        
                        if hashed_word == hash_to_crack:
                            print(f"Hash cracked: {word}")
                            break
                    else:
                        print("Hash not found in wordlist.")
                        
            except Exception as e:
                print(f"An error occurred: {e}")
                if input("Press 'Enter' to return to the main menu or 'q' to quit: ") == 'q':
                    break
                
        elif choice == "2":
            break
            
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
    print("Goodbye!")

def print_ascii_cat(tool_name):
    print(r'''
 /\_/\  
( o.o ) 
 > ^ <  ''', tool_name, "\n")

if __name__ == "__main__":
    main()

