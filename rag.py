from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_mongodb import MongoDBChatMessageHistory  # Updated import
import os

load_dotenv()
mongodb_connection_string = os.getenv("MONGODB_CONNECTION")
chat_history = MongoDBChatMessageHistory(
    session_id="crowwd_01",
    connection_string=mongodb_connection_string,
    database_name="Crowwd",
    collection_name="chat_collection"
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.3
)

system_message = SystemMessage(content="")

def get_response(prompt: str, memory):
    query = HumanMessage(content=prompt)
    memory.add_message(query)
    
    messages = memory.messages
    
    # Pass the list of messages to the model
    response = model.invoke(messages)
    
    memory.add_message(AIMessage(content=response.content))
    return response.content

# print(get_response("hello", chat_history))
