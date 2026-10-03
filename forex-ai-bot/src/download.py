import argparse
from pathlib import Path

import MetaTrader5 as mt5
import pandas as pd

from .market_data import initialize, shutdown, timeframe


def download_rates(symbol: str, timeframe_name: str, candles: int, output: str) -> None:
    initialize()
    try:
        if not mt5.symbol_select(symbol, True):
            raise RuntimeError(f"Unable to select symbol {symbol}")

        rates = mt5.copy_rates_from_pos(
            symbol,
            timeframe(timeframe_name),
            0,
            candles,
        )
        if rates is None or len(rates) == 0:
            raise RuntimeError(f"No data returned: {mt5.last_error()}")

        df = pd.DataFrame(rates)
        df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)

        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
        print(f"Saved {len(df)} candles to {path}")
    finally:
        shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="EURUSD")
    parser.add_argument("--timeframe", default="M5")
    parser.add_argument("--candles", type=int, default=10000)
    parser.add_argument("--output", default="data/EURUSD_M5.csv")
    args = parser.parse_args()

    download_rates(args.symbol, args.timeframe, args.candles, args.output)
