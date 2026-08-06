from fastapi import FastAPI, status
from model import AccountCreate, Transaction
from service import bank_service
app = FastAPI(
    title="Banking REST API"
)
@app.get("/")# decorator 
def home():
    return {
        "message": "Welcome to Banking REST API"
    }
# Create Account
@app.post(
    "/accounts",
    status_code=status.HTTP_201_CREATED
)
def create_account(account: AccountCreate):
    return bank_service.create_account(account)
# Deposit the  money
@app.post("/accounts/{account_number}/deposit")
def deposit_money(
        account_number: str,
        transaction: Transaction
): 
    return bank_service.deposit(
        account_number,
        transaction.amount
    )
# Withdraw the money
@app.post("/accounts/{account_number}/withdraw")
def withdraw_money(
        account_number: str,
        transaction: Transaction
):
    return bank_service.withdraw(
        account_number,
        transaction.amount
    )

@app.get("/accounts/{account_number}")
def get_account(account_number: str):
    return bank_service.get_account(account_number)
# Get All Accounts
@app.get("/accounts")
def get_all_accounts():
    return bank_service.get_all_accounts()