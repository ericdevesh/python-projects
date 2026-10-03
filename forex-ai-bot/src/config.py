import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

TIMEFRAMES = {
    "M1": "TIMEFRAME_M1",
    "M5": "TIMEFRAME_M5",
    "M15": "TIMEFRAME_M15",
    "M30": "TIMEFRAME_M30",
    "H1": "TIMEFRAME_H1",
    "H4": "TIMEFRAME_H4",
    "D1": "TIMEFRAME_D1",
}


@dataclass(frozen=True)
class Settings:
    symbol: str = os.getenv("SYMBOL", "EURUSD")
    timeframe: str = os.getenv("TIMEFRAME", "M5")
    candles: int = int(os.getenv("CANDLES", "300"))
    risk_per_trade: float = float(os.getenv("RISK_PER_TRADE", "0.005"))
    max_daily_loss: float = float(os.getenv("MAX_DAILY_LOSS", "0.02"))
    min_risk_reward: float = float(os.getenv("MIN_RISK_REWARD", "2.0"))


settings = Settings()
