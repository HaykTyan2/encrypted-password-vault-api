import os
from src.core.crypto import derive_key, encrypt_secret, decrypt_secret

def encrypt_entry(secret: str, master_password: str):
    salt = os.urandom(16)
    key = derive_key(master_password, salt)
    encrypted = encrypt_secret(secret, key)
    return encrypted, salt

def decrypt_entry(encrypted: str, master_password: str, salt: bytes):
    key = derive_key(master_password, salt)
    return decrypt_secret(encrypted, key)
