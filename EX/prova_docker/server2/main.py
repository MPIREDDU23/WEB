from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/proxy")
async def proxy():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://server1:8000/")
        return {"proxy_response": response.json()}