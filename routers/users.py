from fastapi import APIRouter
from routers.basemodels import StartUpDetails, DistributionDetails, ExitDetails
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
        distribution_details = {"emails": [], "profit": [], "first":[], "startup_name": []}
        raised = project_collection.find_one({"project_id": dist_data["project_id"]})["raised"]
        startup_name = project_collection.find_one({"project_id": dist_data["project_id"]})["name"]
        for investor in investors:
            invested = investor["amount"]
            profit = calculate_investment_details(invested, raised)
            print(profit)
            email = owner_collection.find_one({"ext_id": investor["ext_id"]})["email"]
            firstname = owner_collection.find_one({"ext_id": investor["ext_id"]})["first"]
            distribution_details["emails"].append(email)
            distribution_details["startup_name"].append(startup_name)
            distribution_details["first"].append(firstname)
            distribution_details["profit"].append(profit)
        return distribution_details

    except Exception as e:
        # Log the error
        print("Error:", e)
        return {"success": False, "message": "Failed to distribute funds"}
    
@router.post("/withdraw")
async def withdraw_funds(details: ExitDetails):
    try:
        # Log the incoming request payload
        print("Incoming payload:", details.model_dump())

        # Process the data
        exit_data = details.model_dump()
        ext_id = exit_data["ext_id"]
        project_id = exit_data["project_id"]

        # Find and delete the matching transaction
        result = transaction_collection.delete_one({"ext_id": ext_id, "project_id": project_id})
        
        if result.deleted_count > 0:
            return {"success": True, "message": "Funds withdrawn successfully."}
        else:
            return {"success": False, "message": "No matching transaction found."}

    except Exception as e:
        # Log the error
        print("Error:", e)
        return {"success": False, "message": "Failed to withdraw funds"}


    

    
