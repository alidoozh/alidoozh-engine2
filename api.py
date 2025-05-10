from fastapi import FastAPI, Body
from signal_engine import get_signals
from decision_engine import get_final_signal
from live_data import get_live_rates
import requests, os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "alidoozh-engine live"}

@app.get("/signal/final")
def final():
    return {"signal": get_final_signal()}

@app.get("/live/rates")
def live():
    return get_live_rates()

@app.post("/telegram/send")
def send(text: dict = Body(...)):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    message = text.get("text", "")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message})
    return {"sent": message}
