# Forex AI Bot

A local, risk-controlled forex research and paper-trading foundation built with Python and MetaTrader 5.

## Current scope

- Connect to an installed MetaTrader 5 terminal
- Read OHLCV/tick data
- Calculate EMA, RSI and ATR
- Generate a transparent BUY/SELL/WAIT signal
- Calculate risk-based position sizing
- Log signals locally
- **No live order execution in this first version**

## Safety

This project does not guarantee profits. It is intentionally built in paper/research mode first. Live execution should only be added after backtesting, out-of-sample testing and demo-forward testing.

## Setup

1. Install MetaTrader 5 and log into a demo account.
2. Install Python 3.11+.
3. From this directory:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

4. Run:

```bash
python -m src.main
```

The app reads the selected symbol and prints the latest market snapshot and signal.

## Configuration

Copy `.env.example` to `.env` and adjust values. Do not commit credentials.

## Roadmap

1. Market-data adapter
2. Strategy engine
3. Backtesting engine
4. Risk manager
5. Demo execution adapter
6. Dashboard
7. Walk-forward/ML research
8. Optional live execution behind explicit safety gates
