from pathlib import Path
import MetaTrader5 as mt5

from .config import settings
from .indicators import add_indicators
from .market_data import get_ohlcv, initialize, shutdown
from .strategy import generate_signal


def main() -> None:
    initialize()
    try:
        df = get_ohlcv(settings.symbol, settings.timeframe, settings.candles)
        enriched = add_indicators(df)
        signal = generate_signal(enriched)
        latest = enriched.iloc[-1]

        account = mt5.account_info()

        print("\n=== FOREX AI BOT / RESEARCH MODE ===")
        print(f"Symbol:       {settings.symbol}")
        print(f"Timeframe:    {settings.timeframe}")
        print(f"Last candle:  {latest['time']}")
        print(f"Bid/close:    {latest['close']:.6f}")
        print(f"EMA20:        {latest['ema20']:.6f}")
        print(f"EMA50:        {latest['ema50']:.6f}")
        print(f"RSI14:        {latest['rsi14']:.2f}")
        print(f"ATR14:        {latest['atr14']:.6f}")
        print(f"Signal:       {signal.action}")
        print(f"Confidence:   {signal.confidence:.0%}")
        print(f"Reason:       {signal.reason}")

        if account:
            print(f"Account mode: {account.trade_mode}")
            print(f"Balance:      {account.balance:.2f}")
            print(f"Equity:       {account.equity:.2f}")

        print("\nNo order was sent. This version is research-only.")
    finally:
        shutdown()


if __name__ == "__main__":
    main()
