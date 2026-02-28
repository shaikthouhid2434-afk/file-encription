from key_manager import generate_key, load_key
from cryptography.fernet import Fernet

# Generate a key with a password
password = 'test123'
generate_key(password)

# Try to load it
try:
    key = load_key(password)
    print(f'Key type: {type(key)}')
    print(f'Key length: {len(key)}')
    
    # Try to create Fernet with it
    fernet = Fernet(key)
    print('Fernet instance created successfully')
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
    import traceback
    traceback.print_exc()
