# 💸 CBDC Wallet API

A simple backend project that simulates a Central Bank Digital Currency (CBDC) wallet using FastAPI.

## 🌐 Live Demo

Test it here:  
🔗 [Swagger UI (Replit)](https://d5320af4-01e5-4798-a5ac-63b71b7cdc08-00-4qol32917fza.sisko.replit.dev/docs)

---

## ✅ Features

- Create wallets
- Simulate sending e₹ between wallets
- Check balances
- Track transaction history

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/cbdc-wallet.git
cd cbdc-wallet
pip install -r requirements.txt
uvicorn main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

---

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/` | Health check |
| POST   | `/wallet/create` | Create new wallet |
| GET    | `/wallet/{wallet_id}` | Get wallet balance |
| POST   | `/wallet/send` | Send funds |
| GET    | `/wallet/{wallet_id}/history` | Transaction history |
