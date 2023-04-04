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

            try:
                with open(wordlist_path, "r", encoding=encoding) as f:
                    for word in f:
                        word = word.strip()
                        hashed_word = hashlib.md5(word.encode(encoding)).hexdigest()
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
