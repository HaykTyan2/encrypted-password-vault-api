from datetime import datetime
from jose import jwt, JWTError
from passlib.context import CryptContext

from src.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_access_token(subject: str = "master") -> str:
    payload = {
        "sub": subject,
        "exp": datetime.utcnow() + ACCESS_TOKEN_EXPIRE,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        subject = payload.get("sub")
        if subject is None:
            raise JWTError()
        return subject
    except JWTError:
        raise





# Passlib is a high-level password security library that exists to 
# prevent developers from misusing cryptographic algorithms like bcrypt,
# which is the actual low-level password hashing algorithm used to securely 
# transform passwords in a one-way, slow, and irreversible manner. 
# When we install passlib[bcrypt], we are telling Python to install passlib 
# along with its optional bcrypt engine, because passlib itself supports many
# algorithms and does not include bcrypt by default. Inside passlib, 
# CryptContext acts as a centralized rule manager or policy controller that defines 
# how passwords should be hashed and verified, including which algorithm to use, 
# how strong it should be, how salts are generated, and how hashes can be upgraded 
# in the future. By creating a CryptContext configured with bcrypt, we 
# avoid directly calling bcrypt or handling sensitive cryptographic details 
# ourselves. When pwd_context.hash(password) is called, CryptContext automatically
# uses bcrypt internally to generate a salt, apply the correct work factor, 
# and return a single encoded hash string containing all necessary metadata. 
# Later, pwd_context.verify(password, hash) safely re-hashes input and compares 
# results without ever decrypting anything. This layered design ensures that 
# plaintext passwords are never stored, security defaults are always correct, 
# and application code remains clean, safe, and future-proof.