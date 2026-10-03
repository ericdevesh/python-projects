from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class Signal:
    action: str
    confidence: float
    reason: str


def generate_signal(df: pd.DataFrame) -> Signal:
    if len(df) < 2:
        return Signal("WAIT", 0.0, "Not enough data")

    row = df.iloc[-1]

    bullish = row["close"] > row["ema20"] > row["ema50"] and 50 < row["rsi14"] < 70
    bearish = row["close"] < row["ema20"] < row["ema50"] and 30 < row["rsi14"] < 50

    if bullish:
        return Signal("BUY", 0.70, "Price above EMA20/EMA50 with positive RSI regime")

    if bearish:
        return Signal("SELL", 0.70, "Price below EMA20/EMA50 with negative RSI regime")

    return Signal("WAIT", 0.0, "Trend/momentum conditions not aligned")
