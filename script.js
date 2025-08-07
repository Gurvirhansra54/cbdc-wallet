const BASE_URL = "https://d5320af4-01e5-4798-a5ac-63b71b7cdc08-00-4qol32917fza.sisko.replit.dev";

async function createWallet() {
  const name = document.getElementById("walletName").value;
  const res = await fetch(`${BASE_URL}/wallet/create`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name })
  });
  const data = await res.json();
  document.getElementById("walletId").innerText = data.wallet_id || "Error";
}

async function getBalance() {
  const walletId = document.getElementById("balanceWalletId").value;
  const res = await fetch(`${BASE_URL}/wallet/${walletId}`);
  const data = await res.json();
  document.getElementById("balance").innerText = data.balance !== undefined ? data.balance : "Error";
}

async function sendMoney() {
  const senderId = document.getElementById("senderId").value;
  const receiverId = document.getElementById("receiverId").value;
  const amount = parseFloat(document.getElementById("amount").value);
  const res = await fetch(`${BASE_URL}/wallet/send`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sender_id: senderId, receiver_id: receiverId, amount })
  });
  const data = await res.json();
  document.getElementById("sendStatus").innerText = data.message || data.error || "Transaction failed";
}
