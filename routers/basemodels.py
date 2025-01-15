from pydantic import BaseModel, EmailStr

class ClerkDetails(BaseModel):
    ext_id: str
    first: str
    last: str
    email: EmailStr  
    pic_url: str
    onboarding_complete: bool = False

class UserDetails(BaseModel):
    ext_id: str
    pan: str
    bank_account: str
    bank_ifsc : str

class StartUpDetails(BaseModel):
    ext_id: str
    name: str
    tan: str
    reg_no: str
    address: str
    description: str
    logo_url: str
    incoperate_cert: str
    pitch_deck: str





