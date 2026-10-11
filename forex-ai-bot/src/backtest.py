from dataclasses import dataclass
import pandas as pd

from .indicators import add_indicators
from .strategy import generate_signal


@dataclass(frozen=True)
class Trade:
    entry_time: object
    exit_time: object
    side: str
    entry: float
    exit: float
    pnl_r: float


@dataclass(frozen=True)
class BacktestResult:
    trades: list[Trade]
    total_r: float
    win_rate: float
    profit_factor: float
    max_drawdown_r: float


def run_backtest(
    raw: pd.DataFrame,
    stop_atr: float = 1.0,
    reward_risk: float = 2.0,
) -> BacktestResult:
    """Simple bar-based research backtest.

    Entry is taken at the next bar open after a signal.
    Exit uses fixed ATR-based SL/TP. If both SL and TP are touched
    within the same candle, the conservative SL-first assumption is used.
    This is deliberately simple; a tick-level engine can replace it later.
    """
    df = add_indicators(raw)
    trades: list[Trade] = []

    i = 0
    while i < len(df) - 1:
        signal = generate_signal(df.iloc[: i + 1])
        if signal.action not in {"BUY", "SELL"}:
            i += 1
            continue

        entry_row = df.iloc[i + 1]
        entry = float(entry_row["open"])
        atr = float(df.iloc[i]["atr14"])
        risk = atr * stop_atr
        if risk <= 0:
            i += 1
            continue

        if signal.action == "BUY":
            stop = entry - risk
            target = entry + risk * reward_risk
        else:
            stop = entry + risk
            target = entry - risk * reward_risk

        exit_price = None
        exit_idx = None

        for j in range(i + 1, len(df)):
            bar = df.iloc[j]
            if signal.action == "BUY":
                hit_stop = bar["low"] <= stop
                hit_target = bar["high"] >= target
                if hit_stop:
                    exit_price, exit_idx = stop, j
                    break
                if hit_target:
                    exit_price, exit_idx = target, j
                    break
            else:
                hit_stop = bar["high"] >= stop
                hit_target = bar["low"] <= target
                if hit_stop:
                    exit_price, exit_idx = stop, j
                    break
                if hit_target:
                    exit_price, exit_idx = target, j
                    break

        if exit_price is None:
            exit_idx = len(df) - 1
            exit_price = float(df.iloc[-1]["close"])

        pnl_r = (
            (exit_price - entry) / risk
            if signal.action == "BUY"
            else (entry - exit_price) / risk
        )

        trades.append(
            Trade(
                entry_time=entry_row["time"],
                exit_time=df.iloc[exit_idx]["time"],
                side=signal.action,
                entry=entry,
                exit=float(exit_price),
                pnl_r=float(pnl_r),
            )
        )
        i = max(exit_idx, i + 1)

    result_values = [t.pnl_r for t in trades]
    total_r = sum(result_values)
    wins = [x for x in result_values if x > 0]
    losses = [-x for x in result_values if x < 0]

    equity = pd.Series([0.0] + list(pd.Series(result_values).cumsum()))
    drawdown = equity - equity.cummax()
    max_dd = abs(float(drawdown.min())) if len(drawdown) else 0.0

    return BacktestResult(
        trades=trades,
        total_r=float(total_r),
        win_rate=float(len(wins) / len(result_values)) if result_values else 0.0,
        profit_factor=float(sum(wins) / sum(losses)) if losses else float("inf"),
        max_drawdown_r=max_dd,
    )
