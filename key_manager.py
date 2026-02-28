from cryptography.fernet import Fernet
import os
import base64
import hashlib

KEY_PATH = "keys/master.key"

def _derive_key_from_password(password: str):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def generate_key(password):
    key = Fernet.generate_key()
    secret = Fernet(_derive_key_from_password(password)).encrypt(key)

    os.makedirs("keys", exist_ok=True)
    with open(KEY_PATH, "wb") as f:
        f.write(secret)

    print("✅ Encrypted master key saved.")

def load_key(password):
    if not os.path.exists(KEY_PATH):
        raise FileNotFoundError("Master key not found. Generate key first.")

    with open(KEY_PATH, "rb") as f:
        encrypted_key = f.read()

    return Fernet(_derive_key_from_password(password)).decrypt(encrypted_key)