from fastapi import FastAPI
from config.settings import conf
from v1.product.router import router as product_router
from database.db import engine

try:
    engine.connect()
    print(".............................Database connection successful!....................................")
except Exception as e:
    print(f"Database connection failed: {e}")



app = FastAPI()



app.include_router(product_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=conf.HOST_URL, port=conf.HOST_PORT)
