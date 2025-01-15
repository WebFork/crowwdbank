from fastapi import APIRouter
from routers.basemodels import UserDetails


router = APIRouter(prefix="/webhook")

@router.post("/clerk")
async def clerk(details:UserDetails):
    try:
        owener_data = UserDetails.model_dump()
        UserDetails.insert_one(owener_data)
        return True
    except Exception as e:
        print("User details are not entered succesfully")
        return False
    
