import os
from dotenv import load_dotenv
import bcrypt
import jwt

# Load environment variables from .env file
load_dotenv()

# Hash a password
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    bytes = password.encode('utf-8')
    hash = bcrypt.hashpw(bytes,salt)  
    hased_password = hash.decode('utf-8') # hashed password
    return hased_password

# Verify a hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password_bytes = plain_password.encode('utf-8')
    is_match = bcrypt.checkpw(plain_password_bytes,hashed_password.encode('utf-8'))
    return is_match

# Create JWT token
def create_access_token(data: dict) -> str:
    # Access JWT_SECRET
    JWT_SECRET = os.getenv("JWT_SECRET")

    if not JWT_SECRET:
        raise ValueError("JWT_SECRET environment variable is not set")
    
    encoded_jwt = jwt.encode(data , JWT_SECRET, algorithm='HS256')
    return encoded_jwt

# Decode JWT token
def verify_token(token: str):
    # Access JWT_SECRET
    JWT_SECRET = os.getenv("JWT_SECRET")

    if not JWT_SECRET:
        raise ValueError("JWT_SECRET environment variable is not set")
    
    payload = jwt.decode(token, JWT_SECRET , algorithms=['HS256'])
    return payload
