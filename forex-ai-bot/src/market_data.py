import MetaTrader5 as mt5
import pandas as pd


def initialize() -> None:
    if not mt5.initialize():
        raise RuntimeError(f"MT5 initialize failed: {mt5.last_error()}")


def shutdown() -> None:
    mt5.shutdown()


def timeframe(name: str):
    value = getattr(mt5, f"TIMEFRAME_{name}", None)
    if value is None:
        raise ValueError(f"Unsupported timeframe: {name}")
    return value


def get_ohlcv(symbol: str, timeframe_name: str, candles: int = 300) -> pd.DataFrame:
    if not mt5.symbol_select(symbol, True):
        raise RuntimeError(f"Unable to select symbol {symbol}")

    rates = mt5.copy_rates_from_pos(
        symbol,
        timeframe(timeframe_name),
        0,
        candles,
    )

    if rates is None or len(rates) == 0:
        raise RuntimeError(f"No market data returned for {symbol}: {mt5.last_error()}")

    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    return df
