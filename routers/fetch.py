from fastapi import APIRouter
from database import project_collection, transaction_collection

router = APIRouter(prefix="/fetch")

@router.get("/projects")
async def fetch_projects():
    projects = project_collection.find()
    list_project = []
    for project in projects:
        project.pop('_id', None)
        list_project.append(project)
    return {"projects": list_project}

@router.get("/with_id")
async def fetch_project_id(project_id: str):
    try:
        project = project_collection.find_one({"project_id": project_id})
        project.pop('_id', None)
        return {"project": project}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/with_user_id")
async def fetch_project_user_id(ext_id: str):
    try:
        project = project_collection.find({"ext_id": ext_id})
        plist = []
        for p in project:
            p.pop('_id', None)
            print(p)
            plist.append(p)
        return {"projects": plist}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/invested_startups")
async def invested_startups(ext_id: str):
    try:
        # Log the incoming request payload
        print("Incoming payload:", ext_id)

        # Process the data
        investors = transaction_collection.find({"ext_id": ext_id})
        invested_startups = {"invested_startups": []}
        seen_projects = set()  # To track unique project IDs

        for investor in investors:
            pr_id = investor["project_id"]
            if pr_id not in seen_projects:  # Check if the project_id is already processed
                startup = project_collection.find_one({"project_id": pr_id})
                if startup:  # Check if the document exists
                    startup.pop('_id', None)  # Remove _id field if it exists
                    invested_startups["invested_startups"].append(startup)
                    seen_projects.add(pr_id)  # Mark this project_id as processed

        return invested_startups

    except Exception as e:
        # Log the error
        print("Error:", e)
        return {"success": False, "message": "Failed to retrieve invested startups"}


    

    


    



