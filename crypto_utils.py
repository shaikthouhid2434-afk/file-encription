from cryptography.fernet import Fernet
from key_manager import load_key

def encrypt_file(file_path, password):
    key = load_key(password)
    fernet = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted)

    print("File encrypted:", file_path + ".enc")


def decrypt_file(enc_file_path, password):
    key = load_key(password)
    fernet = Fernet(key)

    with open(enc_file_path, "rb") as f:
        encrypted_data = f.read()

    decrypted = fernet.decrypt(encrypted_data)

    output_file = enc_file_path.rsplit(".enc", 1)[0] + ".dec"

    with open(output_file, "wb") as f:
        f.write(decrypted)

    print("File decrypted:", output_file)