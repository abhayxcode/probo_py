from fastapi import HTTPException, status
from app.globals.globals import users
from app.models.user import UserCreate, UserSignin
from app.utils.utils import hash_password, verify_password, create_access_token

# --------- Signup user logic ---------
def signup_user(user: UserCreate):
    # Check if user already exists
    for existing_user in users:
        if existing_user['email'] == user.email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    
    # Create a new user and add to in-memory DB
    hashed_password = hash_password(user.password)
    new_user = {"name": user.name, "email": user.email, "password": hashed_password}
    users.append(new_user)
    
    return {"message": "User created successfully"}

# --------- Signin user logic ---------
def signin_user(user: UserSignin):
    # Find user in in-memory DB
    for existing_user in users:
        if existing_user['email'] == user.email:
            if verify_password(user.password, existing_user['password']):
                # Generate JWT token on successful login
                token = create_access_token(data={"email": user.email})
                return {"message": "Login successful", "token": token}
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # If user does not exist
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
