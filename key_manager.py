from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os
import base64

KEY_PATH = "keys/master.key"

def _derive_key_from_password(password: str):
    if not password:
        raise ValueError("Password cannot be empty")
    
    # Use PBKDF2HMAC for secure key derivation with salt
    salt = b"file_encryption_salt"  # In production, use a random salt stored with the key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    derived_key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(derived_key)

def generate_key(password):
    key = Fernet.generate_key()
    secret = Fernet(_derive_key_from_password(password)).encrypt(key)

    os.makedirs("keys", exist_ok=True)
    with open(KEY_PATH, "wb") as f:
        f.write(secret)

    print("Encrypted master key saved.")

def load_key(password):
    if not os.path.exists(KEY_PATH):
        raise FileNotFoundError("Master key not found. Generate key first.")

    with open(KEY_PATH, "rb") as f:
        encrypted_key = f.read()

    return Fernet(_derive_key_from_password(password)).decrypt(encrypted_key)