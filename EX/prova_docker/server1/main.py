from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World. this is server 1"}