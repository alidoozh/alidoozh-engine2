
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class BacktestInput(BaseModel):
    symbol: str
    timeframe: str
    start_date: str
    end_date: str

class BacktestRequest(BaseModel):
    signal_strength: str
    input: BacktestInput
    modules: List[str]

@app.post("/backtest/run")
def run_backtest(data: BacktestRequest):
    input_data = data.input
    result = {
        "summary": {
            "symbol": input_data.symbol,
            "timeframe": input_data.timeframe,
            "start_date": input_data.start_date,
            "end_date": input_data.end_date,
            "signal_strength": data.signal_strength,
            "modules_used": data.modules,
            "win_rate": "83%",
            "total_signals": 12
        },
        "signals": [
            {
                "timestamp": "2024-01-01T00:00:00",
                "signal": "buy",
                "score": 0.84,
                "rr": 2.5,
                "result": "win"
            },
            {
                "timestamp": "2024-01-02T00:00:00",
                "signal": "sell",
                "score": 0.78,
                "rr": 3.1,
                "result": "loss"
            }
        ]
    }
    return result
