import requests
import time
import os
import random

TOKEN = os.getenv("TOKEN", "8357477482:AAHEBmvu6JOpgmNviXOB327NjCUdNNWr1nc")
MESSAGES = [
    "Hidden file unlocked 📂 Join to access → [https://rb.gy/r0nx6k]",
    "New secret video just dropped 🔥 Only few people have seen this → [https://rb.gy/r0nx6k]",
    "Exclusive content leaked 😱 Click here before it’s gone 👉 [https://otieu.com/4/9916786]",
]
CHAT_IDS = ["@hellobabe2006", "-1002345678901"]
INTERVAL_MINUTES = int(os.getenv("INTERVAL_MINUTES", "30"))

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id.strip(), "text": text}
    try:
        resp = requests.post(url, data=payload, timeout=10)
        print(f"✓ {text} → {chat_id}")
        return True
    except Exception as e:
        print(f"✗ {chat_id}: {e}")
        return False

if __name__ == "__main__":
    interval = INTERVAL_MINUTES * 60
    while True:
        random_message = random.choice(MESSAGES)
        for chat_id in CHAT_IDS:
            send_message(chat_id, random_message)
        print(f"ඊළඟට {INTERVAL_MINUTES} මිනිත්තුවකින්...")
        time.sleep(interval)
