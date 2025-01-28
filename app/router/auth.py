from fastapi import APIRouter
from fastapi import HTTPException, status
from app.models.user import UserCreate, UserSignin
from app.api.auth import signin_user, signup_user

# Auth Router
auth_router = APIRouter()

@auth_router.post("/signup")
async def signup(user: UserCreate):
    try:
        return signup_user(user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

# Signin endpoint
@auth_router.post("/signin")
async def signin(user: UserSignin):
    try:
        return signin_user(user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
