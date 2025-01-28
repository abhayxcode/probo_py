from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from app.globals.globals import users, inr_balance,stock_balance,order_book

# Resets the in-meory database
async def reset():
    print(users)
    try:  
         # Clear all data
        users.clear()
        inr_balance.clear()
        stock_balance.clear()
        order_book.clear()

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Reset Successful", 
                     "data": {
                         "users":users,
                         "inr_balance": inr_balance,
                         "stock_balance": stock_balance,
                         "orderbook": order_book
                    }},
          )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
