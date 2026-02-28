from crypto_utils import decrypt_file
from key_manager import load_key
import os

password = 'test123'

# Create test files with .enc in the path
test_content = b'Secret data'

# Edge case: filename with .enc in the middle
problematic_file = 'my.enc.backup.enc'
with open(problematic_file, 'wb') as f:
    f.write(test_content)

# Simulate encryption (just write encrypted content)
from cryptography.fernet import Fernet
key = load_key(password)
fernet = Fernet(key)
encrypted = fernet.encrypt(test_content)

with open(problematic_file, 'wb') as f:
    f.write(encrypted)

print(f"Created: {problematic_file}")

# Try to decrypt - see what filename it generates
output_file = problematic_file.replace(".enc", ".dec")
print(f"Output filename would be: {output_file}")

try:
    decrypt_file(problematic_file, password)
    print("Decrypt successful")
    print(f"Files created: {os.listdir('.')}")
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
