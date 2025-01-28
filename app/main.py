from fastapi import FastAPI
from app.router.auth import auth_router
from app.router.testing import reset

# Initialize app
app = FastAPI()

# Clears in-memory data (for testing only)
@app.post("/reset")
async def reset_handler():
  return await reset()

# Routers
app.include_router(auth_router, prefix='/user')

# Admin Router

# Balances Router

# Order Router