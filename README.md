# 💸 CBDC Wallet Simulation (FastAPI + JS)

A full-stack simulation of a Central Bank Digital Currency (CBDC) Wallet built using FastAPI for the backend and vanilla JavaScript/HTML for the frontend.

![Made with Python](https://img.shields.io/badge/Python-FastAPI-blue?logo=python)
![Hosted on Replit](https://img.shields.io/badge/Backend-Replit-lightgrey?logo=replit)
![Hosted on Netlify](https://img.shields.io/badge/Frontend-Netlify-brightgreen?logo=netlify)

---

## 🌐 Live Demo

- 🔗 **Frontend (UI):** [Open Netlify App](https://playful-selkie-5b13e4.netlify.app/)
- 🔗 **Backend (Swagger API):** [Open Replit API Docs](https://d5320af4-01e5-4798-a5ac-63b71b7cdc08-00-4qol32917fza.sisko.replit.dev/docs)

---

## 🧩 Features

- 🏦 Create simulated CBDC wallets with default e₹ balance
- 💸 Send e₹ between wallets
- 📊 Check wallet balance
- 📜 View transaction history (via backend)
- 🌐 Connects frontend to backend using RESTful API

---

## 📁 Project Structure

```
cbdc-wallet/
├── backend/
│   └── main.py               # FastAPI backend
│   └── requirements.txt      # Backend dependencies
│
├── frontend/
│   └── index.html            # Main UI
│   └── style.css             # Styling
│   └── script.js             # API interactions
│
└── README.md
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cbdc-wallet.git
cd cbdc-wallet
```

### 2. Run Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will be available at `http://localhost:8000/docs`

### 3. Run Frontend

```bash
cd ../frontend
open index.html
```

Or simply double-click `index.html` to open in browser.

---

## 🧪 Sample Test Flow

1. Create two wallets
2. Use `/wallet/send` to transfer funds between them
3. Check both balances and view transaction history

---

## 💡 Tech Stack

- **FastAPI** (Python)
- **HTML + CSS + JS** (Vanilla frontend)
- **Replit** (Backend hosting)
- **Netlify** (Frontend hosting)

---

## 👨‍💻 Author

Built by [Gurvir Singh](https://github.com/Gurvirhansra54) — exploring blockchain, backend systems, and product building.

---

## 📬 Contact

Feel free to connect or share feedback:
- LinkedIn: [Gurvir hansra](https://www.linkedin.com/in/gurvir-singh-bca/)
- GitHub: [@Gurvirhansra54](https://github.com/Gurvirhansra54)

---

⭐ Star the repo if you liked the project!
