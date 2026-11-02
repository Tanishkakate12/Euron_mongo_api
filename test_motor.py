
import asyncio
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv(override=True)

async def test_connection():
    uri = os.getenv("MONGO_URI")

    if not uri:
        print("ERROR: MONGO_URI not found in .env")
        return

    client = AsyncIOMotorClient(
        uri,
        serverSelectionTimeoutMS=10000
    )

    try:
        result = await client.admin.command("ping")
        print("MongoDB connection successful:", result)
    except Exception as e:
        print("MongoDB connection failed:", repr(e))
    finally:
        client.close()

asyncio.run(test_connection())

