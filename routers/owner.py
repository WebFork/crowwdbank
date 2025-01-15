from fastapi import APIRouter
from routers.basemodels import OwnerDetails
from database import owner_collection

router = APIRouter(prefix="/owner")

@router.post("/profile-create")
async def profile_save(details:OwnerDetails):
    try:
        owener_data = OwnerDetails.model_dump()
        owner_collection.insert_one(owener_data)
        return True
    except Exception as e:
        print("User details are not entered succesfully")
        return False
    






