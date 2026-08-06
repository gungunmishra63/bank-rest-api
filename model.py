from pydantic import BaseModel, Field
#basemodel is used to create requests from user and validate them
class AccountCreate(BaseModel):
    account_number: str
    account_holder_name: str = Field(..., min_length=1)
    initial_balance: float = Field(..., ge=0)

class Transaction(BaseModel):
    amount: float = Field(..., gt=0)
 
class Account(BaseModel):
    account_number: str
    account_holder_name: str
    balance: float
