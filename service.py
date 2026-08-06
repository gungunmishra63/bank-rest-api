from fastapi import HTTPException
from model import Account

class BankService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account):

        if account.account_number in self.accounts:
            raise HTTPException(
                status_code=409,
                detail="Account already exists"
            )

        new_account = Account(
            account_number=account.account_number,
            account_holder_name=account.account_holder_name,
            balance=account.initial_balance
        )

        self.accounts[account.account_number] = new_account

        return new_account

    def deposit(self, account_number, amount):

        account = self.accounts.get(account_number)

        if not account:
            raise HTTPException(
                status_code=404,
                detail="Account not found"
            )

        account.balance += amount

        return account

    def withdraw(self, account_number, amount):

        account = self.accounts.get(account_number)

        if not account:
            raise HTTPException(
                status_code=404,
                detail="Account not found"
            )

        if account.balance < amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient balance"
            )

        account.balance -= amount

        return account

    def get_account(self, account_number):

        account = self.accounts.get(account_number)

        if not account:
            raise HTTPException(
                status_code=404,
                detail="Account not found"
            )

        return account

    def get_all_accounts(self):
        return list(self.accounts.values())
bank_service = BankService()