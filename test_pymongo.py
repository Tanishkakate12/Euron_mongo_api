import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(override=True)

uri = os.getenv("MONGO_URI")

if not uri:
    print("MONGO_URI not found")
else:
    client = MongoClient(
        uri,
        serverSelectionTimeoutMS=10000
    )

    try:
        result = client.admin.command("ping")
        print("PyMongo connection successful:", result)

    except Exception as e:
        print("PyMongo connection failed:", repr(e))

    finally:
        client.close()