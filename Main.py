
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import os
# from motor.motor_asyncio import AsyncIOMotorClient
# from dotenv import load_dotenv
# from urllib.parse import quote_plus
# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")

# client = AsyncIOMotorClient( MONGO_URI)

# db = client["euron"]
# euron_data = db["euron_coll"]

# app = FastAPI()

# class euron(BaseModel):
#     name: str
#     phone: int
#     city: str
#     course: str

# @app.post("/euron/insert")
# async def euron_data_insert_helper(data:euron):
#     result = await euron_data.insert_one(data.model_dump())  
#     return {
#         "message": "Data insert successfully",
#         "id": str(result.inserted_id)
#     # }

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI is missing from the .env file")

client = AsyncIOMotorClient(
    MONGO_URI,
    serverSelectionTimeoutMS=10000
)

db = client["euron"]
euron_data = db["euron_coll"]

app = FastAPI()


class Euron(BaseModel):
    name: str
    phone: int
    city: str
    course: str


@app.get("/")
async def home():
    return {"message": "Euron API is running"}


@app.post("/euron/insert")
async def euron_data_insert_helper(data: Euron):
    try:
        # Check that MongoDB is reachable
        await client.admin.command("ping")

        # Insert the document
        result = await euron_data.insert_one(data.model_dump())

        return {
            "message": "Data inserted successfully",
            "id": str(result.inserted_id)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

