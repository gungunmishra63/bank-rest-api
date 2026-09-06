# 🏦 Banking REST API

<div align="center">

### 💳 A Simple Banking Backend built with FastAPI

A REST API Banking Application built using **Python, FastAPI and Pydantic**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063)
![Uvicorn](https://img.shields.io/badge/Uvicorn-Server-purple)

</div>

---

## 📖 About the Project

The **Banking REST API** is a backend application developed using **Python and FastAPI** to simulate basic banking operations through RESTful API endpoints.

The application allows users to:

* 🏦 Create an account
* 💰 Deposit money
* 💸 Withdraw money
* 👤 Get account details
* 📋 Get all accounts

The project demonstrates how a backend application can be divided into **API routes, data models, and business logic**.

Account information is currently maintained in memory using a Python dictionary, making this project suitable for learning and demonstrating REST API concepts.

---

## 🎯 Project Objective

The main objective is to understand:

* REST API development
* FastAPI application structure
* HTTP methods
* Request and response handling
* Data validation using Pydantic
* Business logic implementation
* API error handling
* Interactive API testing using Swagger UI

---

# 🚀 Features

| Feature                | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| 🏦 Create Account      | Creates a new bank account                                            |
| 💰 Deposit Money       | Adds money to an existing account                                     |
| 💸 Withdraw Money      | Withdraws money from an account                                       |
| 👤 Get Account Details | Retrieves a specific account                                          |
| 📋 Get All Accounts    | Retrieves all accounts                                                |
| ✅ Validation           | Validates request data using Pydantic                                 |
| ⚠️ Error Handling      | Handles duplicate accounts, missing accounts and insufficient balance |

---

# 🛠️ Technology

| Technology | Purpose                   |
| ---------- | ------------------------- |
| 🐍 Python  | Programming Language      |
| ⚡ FastAPI  | REST API Framework        |
| ✅ Pydantic | Request & Data Validation |
| 🚀 Uvicorn | ASGI Server               |

---

# 🧩 Project Architecture

```text
                    👤 Client
                       │
                       ▼
                  ⚡ FastAPI
                       │
                 ┌─────┴─────┐
                 ▼           ▼
             model.py     service.py
                 │           │
          Data Validation    │
                 │           │
                 └─────┬─────┘
                       ▼
                🏦 Account Data
                 (In-Memory)
                       │
                       ▼
                 API Response
```

### 📄 File Responsibilities

```text
bank-rest-api/
│
├── main.py
├── model.py
├── service.py
└── README.md
```

### `main.py`

Contains the FastAPI application and API endpoints.

It defines routes for:

* Creating accounts
* Depositing money
* Withdrawing money
* Getting account details
* Getting all accounts

### `model.py`

Contains Pydantic models used for request validation and account data representation.

### `service.py`

Contains the main banking business logic such as:

* Creating accounts
* Checking duplicate accounts
* Depositing money
* Withdrawing money
* Checking account existence
* Checking sufficient balance

---

# 💻 Main Code

## 1️⃣ FastAPI Application

The FastAPI application is initialized in `main.py`.

```python
from fastapi import FastAPI, status

app = FastAPI(
    title="Banking REST API"
)
```

This creates the main API application and gives it the title **Banking REST API**.

---

## 2️⃣ Pydantic Models

`model.py` uses Pydantic's `BaseModel` and `Field` for validation.

```python
from pydantic import BaseModel, Field

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
```

### Validation used

* Account holder name must contain at least one character.
* Initial balance cannot be negative.
* Transaction amount must be greater than zero.

---

# 🏦 API Endpoints

## 1. Create Account

```http
POST /accounts
```

```python
@app.post(
    "/accounts",
    status_code=status.HTTP_201_CREATED
)
def create_account(account: AccountCreate):
    return bank_service.create_account(account)
```

Creates a new account and returns the created account.

---

## 2. Deposit Money

```http
POST /accounts/{account_number}/deposit
```

```python
@app.post("/accounts/{account_number}/deposit")
def deposit_money(
    account_number: str,
    transaction: Transaction
):
    return bank_service.deposit(
        account_number,
        transaction.amount
    )
```

The requested amount is added to the selected account balance.

---

## 3. Withdraw Money

```http
POST /accounts/{account_number}/withdraw
```

```python
@app.post("/accounts/{account_number}/withdraw")
def withdraw_money(
    account_number: str,
    transaction: Transaction
):
    return bank_service.withdraw(
        account_number,
        transaction.amount
    )
```

The API checks whether the account exists and whether sufficient balance is available before withdrawing money.

---

## 4. Get Account Details

```http
GET /accounts/{account_number}
```

```python
@app.get("/accounts/{account_number}")
def get_account(account_number: str):
    return bank_service.get_account(account_number)
```

Returns information about a particular account.

---

## 5. Get All Accounts

```http
GET /accounts
```

```python
@app.get("/accounts")
def get_all_accounts():
    return bank_service.get_all_accounts()
```

Returns all accounts currently available in the application.

---

# ⚙️ Banking Business Logic

The main business logic is implemented inside `service.py`.

### Create Account

```python
if account.account_number in self.accounts:
    raise HTTPException(
        status_code=409,
        detail="Account already exists"
    )
```

This prevents duplicate account numbers.

### Deposit

```python
account.balance += amount
```

The deposited amount is added to the current balance.

### Withdraw

```python
if account.balance < amount:
    raise HTTPException(
        status_code=400,
        detail="Insufficient balance"
    )

account.balance -= amount
```

The application prevents withdrawals when the account does not have sufficient balance.

---

# 🔄 Project Workflow

```text
          👤 User
            │
            ▼
       HTTP Request
            │
            ▼
        FastAPI
            │
            ▼
     Pydantic Validation
            │
            ▼
      BankService
            │
       ┌────┴────┐
       ▼         ▼
   Account    Transaction
   Operation   Operation
       │         │
       └────┬────┘
            ▼
      Updated Account
            │
            ▼
       API Response
```

---

# 📡 API Summary

| Method | Endpoint                              | Purpose             |
| ------ | ------------------------------------- | ------------------- |
| `GET`  | `/`                                   | Welcome message     |
| `POST` | `/accounts`                           | Create account      |
| `POST` | `/accounts/{account_number}/deposit`  | Deposit money       |
| `POST` | `/accounts/{account_number}/withdraw` | Withdraw money      |
| `GET`  | `/accounts/{account_number}`          | Get account details |
| `GET`  | `/accounts`                           | Get all accounts    |

---

# 📦 Installation

Install the required packages:

```bash
pip install fastapi uvicorn pydantic
```

### Required Packages

* **FastAPI** – REST API framework
* **Uvicorn** – Application server
* **Pydantic** – Data validation

---

# ▶️ Run

Start the application using:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

The `--reload` option automatically reloads the server when code changes are made.

---

# 📖 Swagger UI

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

* 🔍 View all endpoints
* ✏️ Enter request data
* ▶️ Execute API requests
* 📥 View responses
* 🧪 Test banking operations

---

# 🧪 Testing Flow

```text
Start Server
     ↓
Open Swagger UI
     ↓
Create Account
     ↓
Deposit Money
     ↓
Withdraw Money
     ↓
Get Account Details
     ↓
Get All Accounts
```

---

# 📂 Project Structure

```text
bank-rest-api/
│
├── 🐍 main.py       # FastAPI application & routes
├── 📋 model.py      # Pydantic models & validation
├── ⚙️ service.py    # Banking business logic
└── 📖 README.md     # Documentation
```

---

# 💡 Learning Outcomes

Through this project, I learned:

* REST API development
* FastAPI framework
* Python backend development
* HTTP methods
* Request and response handling
* Pydantic validation
* Business logic implementation
* Exception handling
* API testing with Swagger UI
* Structuring a backend project

---

# 🔮 Future Enhancements

Possible improvements include:

* 🗄️ Database integration
* 🔐 User authentication
* 👥 User authorization
* 💳 Transaction history
* 🧾 Account statements
* 👨‍💼 Admin functionality
* 🔒 Improved security
* ☁️ Cloud deployment

---

# 👩‍💻 Author

## Gungun Mishra

**MCA Student | Aspiring Software Developer | AI/ML & Web Development**

---

<div align="center">

### ⭐ If you like this project, consider giving it a star!

**Built with ❤️ using Python & FastAPI**

</div>
