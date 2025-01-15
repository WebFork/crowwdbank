from fastapi import APIRouter
from database import project_collection

router = APIRouter(prefix="/fetch")

@router.get("/projects")
async def fetch_projects():
    projects = project_collection.find()
    list_project = []
    for project in projects:
        project.pop('_id', None)
        list_project.append(project)
    return {"projects": list_project}

@router.get("/fetch_with_id/")
async def fetch_project_id(project_id: str):
    try:
        project = project_collection.find_one({"project_id": project_id})
        project.pop('_id', None)
        return {"project": project}
    except Exception as e:
        return {"error": str(e)}


