import os
import sys
import json
from pymongo import MongoClient
from dotenv import load_dotenv

# === Load .env variables ===
load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
DB_NAME = "incidents"
DATA_FOLDER = "./data"

# === Usage check ===
if len(sys.argv) != 2 or sys.argv[1] not in ["positive", "negative"]:
    print("Usage: python3 insert_incidents.py [positive|negative]")
    sys.exit(1)

collection_name = f"{sys.argv[1]}_incidents"

# === MongoDB Connection ===
if not MONGO_USER or not MONGO_PASS:
    print("Mongo credentials not found in .env file.")
    sys.exit(1)

client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}")
db = client[DB_NAME]
collection = db[collection_name]

# === Insert JSON files ===
inserted = 0
for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".json"):
        filepath = os.path.join(DATA_FOLDER, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                doc = json.load(f)

            if "incident_id" in doc:
                doc["_id"] = doc["incident_id"]

            collection.insert_one(doc)
            print(f"✓ Inserted: {filename}")
            inserted += 1

        except Exception as e:
            print(f"✗ Failed to insert {filename}: {e}")

print(f"\nDone. {inserted} document(s) inserted into '{collection_name}' collection.")
