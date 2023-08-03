from fastapi import FastAPI
from mangum import Mangum


app=FastAPI()

@app.get("/")

async def home():
    return {"Message":"Hello Everyone "}

@app.get("/list")

def listall():
    return {"message":"Here is your List"}



