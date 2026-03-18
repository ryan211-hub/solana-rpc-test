import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HELIUS_API_KEY")

RPC = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"

payload = {
    "jsonrpc":"2.0",
    "id":1,
    "method":"getHealth"
}

r = requests.post(RPC, json=payload)

print(r.text)