from fastapi import APIRouter
from routers.basemodels import ClerkDetails, TransactDetails
from database import owner_collection, transaction_collection


router = APIRouter(prefix="/webhook")

@router.post("/clerk")
async def clerk(details:ClerkDetails):
    try:
        owner_data = details.model_dump()
        print(owner_data)
        owner_collection.insert_one(owner_data)
        return True
    except Exception as e:
        print(e)
        print("User details are not entered succesfully")
        return False
    
@router.post("/transact")
async def transact(details:TransactDetails):
    # project_id: str
    # amount: float
    try:
        transaction_data = details.model_dump()
        print(transaction_data)
        transaction_collection.insert_one(transaction_data)
        condition = {"project_id": transaction_data["project_id"]}
        owner_collection.update_one(condition, {"$inc": {"amount": transaction_data["amount"]}})
        return True
    except Exception as e:
        print(e)
        print("User details are not entered succesfully")
        return False

    
