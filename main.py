from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

wallets = {}

class WalletCreate(BaseModel):
    name: str

class TransactionRequest(BaseModel):
    sender_id: str
    receiver_id: str
    amount: float

@app.get("/")
def home():
    return {"message": "CBDC Wallet API is working!"}

@app.post("/wallet/create")
def create_wallet(wallet: WalletCreate):
    wallet_id = str(uuid.uuid4())
    wallets[wallet_id] = {
        "name": wallet.name,
        "balance": 1000.0,
        "transactions": []
    }
    return {"wallet_id": wallet_id, "balance": wallets[wallet_id]["balance"]}

@app.get("/wallet/{wallet_id}")
def get_balance(wallet_id: str):
    if wallet_id not in wallets:
        return {"error": "Wallet not found"}
    return {"wallet_id": wallet_id, "balance": wallets[wallet_id]["balance"]}

@app.post("/wallet/send")
def send_money(txn: TransactionRequest):
    sender = wallets.get(txn.sender_id)
    receiver = wallets.get(txn.receiver_id)

    if not sender or not receiver:
        return {"error": "Sender or receiver not found"}
    if txn.amount <= 0:
        return {"error": "Amount must be greater than 0"}
    if sender["balance"] < txn.amount:
        return {"error": "Insufficient balance"}

    sender["balance"] -= txn.amount
    receiver["balance"] += txn.amount

    sender["transactions"].append({
        "type": "sent",
        "to": txn.receiver_id,
        "amount": txn.amount
    })
    receiver["transactions"].append({
        "type": "received",
        "from": txn.sender_id,
        "amount": txn.amount
    })

    return {
        "message": "Transaction successful",
        "sender_balance": sender["balance"],
        "receiver_balance": receiver["balance"]
    }

@app.get("/wallet/{wallet_id}/history")
def get_history(wallet_id: str):
    wallet = wallets.get(wallet_id)
    if not wallet:
        return {"error": "Wallet not found"}
    return {"wallet_id": wallet_id, "transactions": wallet["transactions"]}
