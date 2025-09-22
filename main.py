import requests
import os
import logging
from datetime import datetime

# Logging සකසන්න
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Environment variables භාවිතා කරන්න
TOKEN = os.environ['8357477482:AAEWeRNnFUl0TOncLTKS57dCQ3tajOqHir4']
CHAT_IDS = os.environ['@hellobabe2006'].split(',')

MESSAGES = [
     "Hidden file unlocked 📂 Join to access → [https://rb.gy/r0nx6k]",
    "New secret video just dropped 🔥 Only few people have seen this → [https://rb.gy/r0nx6k]",
    "Exclusive content leaked 😱 Click here before it’s gone 👉 [https://otieu.com/4/9916786]",
]

def send_telegram_message(chat_id, message):
    """Telegram පණිවිඩය යවන්න"""
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    payload = {
        "chat_id": chat_id.strip(),
        "text": message,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(api_url, json=payload, timeout=15)
        if response.status_code == 200:
            logging.info(f"පණිවිඩය යවන ලදී: {chat_id}")
            return True
        else:
            logging.error(f"දෝෂය: {response.status_code} - {response.text}")
            return False
    except Exception as error:
        logging.error(f"නොගැලපීම: {error}")
        return False

def main():
    """මූලික ක්‍රියාවලිය - එක් වරක් පමණක් run වේ"""
    logging.info("Telegram ස්වයංක්‍රීය පණිවිඩ යවන්නෙක් ආරම්භ කරන ලදී")
    
    # වර්තමාන දිනය අනුව message එක තෝරාගන්න
    day_of_month = datetime.now().day
    message_index = day_of_month % len(MESSAGES)
    current_message = MESSAGES[message_index]
    
    # සියලුම groups වලට පණිවිඩය යවන්න
    for chat_id in CHAT_IDS:
        send_telegram_message(chat_id, current_message)
        logging.info(f"පණිවිඩය යවන ලදී: {chat_id}")
    
    logging.info("කාර්යය සම්පූර්ණයි!")

if __name__ == "__main__":
    main()
