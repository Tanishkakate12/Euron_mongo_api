import os
import asyncio
import certifi
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

async def test_connection():
    try:
        client = AsyncIOMotorClient(
            MONGO_URI,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=10000
        )

        await client.admin.command("ping")

        print("MongoDB Connected Successfully!")

        client.close()

    except Exception as e:
        print("MongoDB Connection Failed!")
        print(type(e).__name__)
        print(e)

asyncio.run(test_connection())