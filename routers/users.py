from fastapi import APIRouter
from routers.basemodels import StartUpDetails
from database import project_collection

router = APIRouter(prefix="/user")

@router.post("/register_startup")
async def register_startup(details:StartUpDetails):
    try:
        startup_data = details.model_dump()
        startup_data["maxInvestment"] = startup_data.target - startup_data.raised
        print(startup_data)
        project_collection.insert_one(startup_data)
        return True
    except Exception as e:
        print(e)
        print("User details are not entered succesfully")
        return False
    