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
- Configurable research cost assumptions for spread, slippage and commission
- Regression tests are included
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

## Research gates

The project is being developed in this order:

1. Historical backtest
2. Transaction-cost assumptions
3. Chronological train/validation/test evaluation
4. Rolling out-of-sample evaluation
5. Demo/paper forward testing
6. Only after evidence supports it, consider a separately gated live-execution module

Do not optimize parameters on the same data used to judge performance.

## Important limitations

The current bar-based backtester does not yet fully apply the configurable cost model to every simulated fill, and it does not model swaps or intra-bar tick ordering. If a candle touches both SL and TP, it assumes SL first. Results are **research estimates, not expected live returns**.

MetaTrader 5's Python integration provides historical bar/tick access through its terminal connection; available history also depends on the terminal's chart-history settings.

## Safety

No broker order is sent by this repository version. Live execution remains disabled until research and demo-testing gates are satisfied.
