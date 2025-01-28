from typing import Optional
from datetime import timedelta

# Hash a password
def hash_password(password: str) -> str:
    return password

# Verify a hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return True

# Create JWT token
def create_access_token(data: dict) -> str:
    return 'token'

# Decode JWT token
def verify_token(token: str):
    return 'payload'
