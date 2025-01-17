from fastapi import APIRouter
from rag import get_response
from routers.basemodels import RAGDetails
from langchain_mongodb import MongoDBChatMessageHistory
import os
from dotenv import load_dotenv


load_dotenv()
mongodb_connection_string = os.getenv("MONGODB_CONNECTION")
router = APIRouter(prefix="/responder")


@router.post("/getresponse")
async def get_respond(data:RAGDetails):
    chat_history = MongoDBChatMessageHistory(
    session_id=data.ext_id,
    connection_string=mongodb_connection_string,
    database_name="Crowwd",
    collection_name="chat_collection"
    )
    knowlege_base = "The start up idea is "+ data.knowledge_base 
    return {"response":get_response(data.prompt, chat_history, knowlege_base)}


