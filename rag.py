from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_mongodb import MongoDBChatMessageHistory
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.docstore.document import Document
import os
import faiss

# Load environment variables
load_dotenv()

# MongoDB chat history setup
mongodb_connection_string = os.getenv("MONGODB_CONNECTION")
chat_history = MongoDBChatMessageHistory(
    session_id="crowwd_01",
    connection_string=mongodb_connection_string,
    database_name="Crowwd",
    collection_name="chat_collection"
)

# Initialize the Google Gemini LLM
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.3
)

# System message setup
system_message = SystemMessage(content="you are a fundamental analysis bot and startup analyser. You can evaluate the idea and provide the analysis to the user")

# Function to process a knowledge base string and create a retriever
def create_retriever_from_string(knowledge_base: str):
    # Convert the knowledge base string into Document objects
    documents = [Document(page_content=knowledge_base)]
    
    # Generate embeddings and create a vector store
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # Adjust model ID if needed
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store.as_retriever()

# Function to get responses with RAG integration
def get_response(prompt: str, memory, knowledge_base: str):
    # Store user query in memory
    query = HumanMessage(content=prompt)
    memory.add_message(query)
    
    # Create a retriever from the knowledge base string
    retriever = create_retriever_from_string(knowledge_base)
    
    # Create the RAG chain for this query
    rag_chain = RetrievalQA.from_chain_type(llm=model, chain_type="stuff", retriever=retriever)
    
    # Retrieve context from the knowledge base using RAG
    retrieved_response = rag_chain.run(prompt)
    
    # Generate a final response using the LLM and context
    response = model.invoke([*memory.messages, HumanMessage(content=retrieved_response)])
    
    # Store LLM response in memory
    memory.add_message(AIMessage(content=response.content))
    return response.content