from fastapi import APIRouter, HTTPException, status
from routers.basemodels import UserDetails
from database import owner_collection

router = APIRouter(prefix="/onboarding")

@router.post("/user_create")
async def user_create(details: UserDetails):
    try:
        condition = {"ext_id": details.ext_id}
        update = { "$set": { "pan": details.pan, "bank_acc": details.bank_account, "ifsc_code": details.bank_ifsc }}
        
        check = owner_collection.find_one(condition)
        
        if check is None:
            
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        owner_collection.update_one(condition, update)
        return {"message": "User updated successfully"}

    except Exception as e:
        print(f"Error in updating user: {e}")  
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating the user"
        )

        

