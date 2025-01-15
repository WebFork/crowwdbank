from pydantic import BaseModel, EmailStr

class OwnerDetails(BaseModel):
    ext_id: str
    first: str
    last: str
    email: EmailStr  
    pic_url: str
    onboarding_complete: bool = False
