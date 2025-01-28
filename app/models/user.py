from pydantic import BaseModel

# User schema for request validation
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

# Signin schema for request validation
class UserSignin(BaseModel):
    email: str
    password: str
