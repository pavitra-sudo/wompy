from fastapi import FastAPI
from config.settings import conf

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to the Wompy API!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=conf.HOST_URL, port=conf.HOST_PORT)
