from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

class BacktestRequest(BaseModel):
    symbol: str
    timeframe: str
    start_date: str
    end_date: str
    signal_strength: str
    modules: List[str]

@app.post("/backtest/run")
def run_backtest(data: BacktestRequest):
    signals = []
    for i in range(10):
        signals.append({
            "timestamp": f"2024-01-{i+1:02d}T00:00:00",
            "signal": random.choice(["buy", "sell"]),
            "score": round(random.uniform(0.7, 0.95), 2),
            "rr": round(random.uniform(2.0, 4.5), 2),
            "result": random.choice(["win", "loss"])
        })

    win_count = sum(1 for s in signals if s["result"] == "win")
    win_rate = round((win_count / len(signals)) * 100, 2)

    return {
        "summary": {
            "symbol": data.symbol,
            "timeframe": data.timeframe,
            "signal_strength": data.signal_strength,
            "modules": data.modules,
            "win_rate": win_rate,
            "total_signals": len(signals)
        },
        "signals": signals
    }
