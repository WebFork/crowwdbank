from fastapi import APIRouter
from routers.basemodels import ClerkDetails
from database import owner_collection


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
    
