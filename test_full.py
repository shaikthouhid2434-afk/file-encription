from key_manager import load_key
from crypto_utils import encrypt_file, decrypt_file
import os

password = 'test123'

# Create a test file
test_file = 'test_file.txt'
with open(test_file, 'w') as f:
    f.write('Hello, this is a secret message!')

# Test encryption
try:
    encrypt_file(test_file, password)
    print("Encryption successful")
except Exception as e:
    print(f'Encryption error: {type(e).__name__}: {e}')
    import traceback
    traceback.print_exc()

# Test decryption
try:
    decrypt_file(test_file + '.enc', password)
    print("Decryption successful")
    
    # Check if decrypted file matches original
    with open(test_file, 'r') as f:
        original = f.read()
    with open(test_file + '.dec', 'r') as f:
        decrypted = f.read()
    
    if original == decrypted:
        print("✓ Decrypted content matches original")
    else:
        print("✗ Decrypted content does NOT match original")
        
except Exception as e:
    print(f'Decryption error: {type(e).__name__}: {e}')
    import traceback
    traceback.print_exc()
