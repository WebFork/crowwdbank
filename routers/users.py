from fastapi import APIRouter
from routers.basemodels import StartUpDetails, DistributionDetails
from database import project_collection, transaction_collection, owner_collection
from routers.helpers import calculate_investment_details

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
    
@router.post("/distribute")
async def distribute_funds(details: DistributionDetails):
    try:
        # Log the incoming request payload
        print("Incoming payload:", details.model_dump())

        # Process the data
        dist_data = details.model_dump()
        investors = transaction_collection.find({"project_id": dist_data["project_id"]})
        distribution_details = {"email": [], "profit": []}
        # raised = project_collection.find_one({"project_id": dist_data["project_id"]})["raised"]

        for investor in investors:
            invested = investor["amount"]
            profit = calculate_investment_details(invested, dist_data["raised"])
            email = owner_collection.find_one({"ext_id": investor["ext_id"]})["email"]
            distribution_details["email"].append(email)
            distribution_details["profit"].append(profit)
        return distribution_details

    except Exception as e:
        # Log the error
        print("Error:", e)
        return {"success": False, "message": "Failed to distribute funds"}
    
