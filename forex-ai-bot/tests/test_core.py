import pandas as pd
from src.indicators import add_indicators
from src.strategy import generate_signal
from src.validation import chronological_split

def sample_data(n=250):
    prices=[1.10+i*0.0001 for i in range(n)]
    return pd.DataFrame({"time":pd.date_range("2026-01-01",periods=n,freq="5min"),
        "open":prices,"high":[p+0.0002 for p in prices],"low":[p-0.0002 for p in prices],
        "close":[p+0.00005 for p in prices],"tick_volume":[1000]*n})

def test_indicators_and_signal():
    df=add_indicators(sample_data())
    assert {"ema20","ema50","rsi14","atr14"}.issubset(df.columns)
    assert generate_signal(df).action in {"BUY","SELL","WAIT"}

def test_chronological_split():
    split=chronological_split(sample_data(),0.6,0.2)
    assert len(split.train)==150 and len(split.validation)==50 and len(split.test)==50
