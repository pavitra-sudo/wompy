from fastapi import FastAPI
from config.settings import conf
from v1.product.router import router as product_router
app = FastAPI()

app.include_router(product_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=conf.HOST_URL, port=conf.HOST_PORT)
