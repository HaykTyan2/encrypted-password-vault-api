import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet

def derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    key = kdf.derive(master_password.encode())
    return base64.urlsafe_b64encode(key)


def encrypt_secret(plaintext: str, key: bytes) -> str:
    fernet = Fernet(key)
    return fernet.encrypt(plaintext.encode()).decode()


def decrypt_secret(ciphertext: str, key: bytes) -> str:
    fernet = Fernet(key)
    return fernet.decrypt(ciphertext.encode()).decode()
