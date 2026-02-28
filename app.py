from key_manager import generate_key
from crypto_utils import encrypt_file, decrypt_file

def menu():
    print("\n1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Choose: ")

    if choice == "1":
        pwd = input("Set master password: ")
        generate_key(pwd)

    elif choice == "2":
        pwd = input("Enter master password: ")
        path = input("Enter file path: ")
        encrypt_file(path, pwd)

    elif choice == "3":
        pwd = input("Enter master password: ")
        path = input("Enter encrypted file path: ")
        decrypt_file(path, pwd)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    while True:
        menu()