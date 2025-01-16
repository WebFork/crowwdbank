from pydantic import BaseModel, EmailStr




class ClerkDetails(BaseModel):
    ext_id: str
    first: str
    last: str
    email: EmailStr  
    pic_url: str
    onboarding_complete: bool = False

class Check(BaseModel):
    ext_id: str

class UserDetails(BaseModel):
    ext_id: str
    pan: str
    bank_account: str
    bank_ifsc : str

class StartUpDetails(BaseModel):
    ext_id: str
    project_id: str
    name: str
    category: str
    target: float
    raised: float = 0
    tan: str
    reg_no: str
    address: str
    description: str
    logo_url: str
    incoperate_cert: str
    pitch_deck: str
    status: str = "Approved"
    valuation: float
    minInvestment: float = 250
    maxInvestment: float = 0



class RAGDetails(BaseModel):
    ext_id: str
    project_id: str
    prompt: str
    knowledge_base: str

class TransactDetails(BaseModel):
    ext_id: str
    project_id: str
    amount: float
    transaction_id: str
    status: str

class DistributionDetails(BaseModel):
    project_id: str
    profit: float














