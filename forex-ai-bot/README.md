# Forex AI Bot

A local, risk-controlled forex research and paper-trading foundation built with Python and MetaTrader 5.

## Current scope

- Connect to MetaTrader 5
- Read OHLCV data
- Calculate EMA, RSI and ATR
- Generate transparent BUY/SELL/WAIT signals
- Run a bar-based historical backtest
- Report win rate, profit factor, total R and maximum drawdown
- Download historical candles from MT5
- Calculate generic risk-based position sizing
- **No live order execution**

## Run

Install:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

Download data from a connected MT5 terminal:

```bash
python -m src.download --symbol EURUSD --timeframe M5 --candles 10000
```

Run the research backtest:

```bash
python -m src.run_backtest --file data/EURUSD_M5.csv
```

Try another risk/reward assumption:

```bash
python -m src.run_backtest --file data/EURUSD_M5.csv --reward-risk 2.5
```

## Important research limitations

This backtester is intentionally conservative and simple. It does not model spread, commissions, swaps, slippage or intra-bar tick ordering. If a candle touches both SL and TP, it assumes SL first. Results are therefore **research estimates, not expected live returns**.

Do not optimize parameters on the same data used to judge performance. The next development stage should add train/validation/test splits, walk-forward evaluation, transaction-cost modeling and demo forward testing.

## Safety

No broker order is sent by this repository version. Live execution remains disabled until the research and demo-testing gates are satisfied.
