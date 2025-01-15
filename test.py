from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

class UserProfile(BaseModel):
    username: str
    email: EmailStr
    bio: Optional[str] = None

@app.post("/create-profile/")
async def create_profile(
    profile_pic: UploadFile = File(...),  # Profile picture
    username: str = Form(...),           # Other fields parsed via Form
    email: EmailStr = Form(...),
    bio: Optional[str] = Form(None),
):
    try:
        # Read and process the profile picture (save or validate, if needed)
        file_content = await profile_pic.read()
        file_size = len(file_content)
        
        if file_size > 2 * 1024 * 1024:  # Example: Limit file size to 2MB
            raise HTTPException(status_code=400, detail="Profile picture too large (max 2MB).")

        # Create a Pydantic model instance with other user data
        user_profile = UserProfile(username=username, email=email, bio=bio)

        return {
            "message": "Profile created successfully!",
            "profile_pic_filename": profile_pic.filename,
            "profile_pic_content_type": profile_pic.content_type,
            "user_data": user_profile.dict(),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
