from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
connection_string = os.getenv("MONGODB_CONNECTION")

mongo_client = MongoClient(connection_string)
db = mongo_client["Crowwd"]
owner_collection = db["owner_collection"]
project_collection = db["project_collection"]
chat_collection = db["chat_collection"]


