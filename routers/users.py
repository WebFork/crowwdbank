from fastapi import APIRouter
from routers.basemodels import StartUpDetails
from database import project_collection

router = APIRouter(prefix="/user")

@router.post("/register_startup")
async def register_startup(details: StartUpDetails):
    try:
        # Log the incoming request payload
        print("Incoming payload:", details.model_dump())

        # Process the data
        startup_data = details.model_dump()
        startup_data["maxInvestment"] = startup_data["target"] - startup_data["raised"]
        
        # Log the processed data
        print("Processed data:", startup_data)

        # Insert into the database
        project_collection.insert_one(startup_data)
        return {"success": True, "message": "Startup registered successfully"}
    except Exception as e:
        # Log the error
        print("Error:", e)
        return {"success": False, "message": "Failed to register startup"}

    