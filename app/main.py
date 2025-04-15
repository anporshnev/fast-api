from fastapi import FastAPI, Body
from fastapi.responses import FileResponse 

app = FastAPI()

@app.get("/")
async def index():
    return {"result": "Hello"}

@app.get("/custom")
async def custom():
    return {"name": "custom"}

