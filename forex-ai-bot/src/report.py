from .backtest import BacktestResult


def print_report(result: BacktestResult) -> None:
    print("\n=== BACKTEST REPORT ===")
    print(f"Trades:          {len(result.trades)}")
    print(f"Total R:         {result.total_r:.2f}")
    print(f"Win rate:        {result.win_rate:.2%}")
    print(f"Profit factor:   {result.profit_factor:.2f}")
    print(f"Max drawdown R:  {result.max_drawdown_r:.2f}")

    if result.trades:
        print("\nLast 5 trades:")
        for trade in result.trades[-5:]:
            print(
                f"{trade.entry_time} | {trade.side:4} | "
                f"{trade.entry:.6f} -> {trade.exit:.6f} | "
                f"{trade.pnl_r:+.2f}R"
            )
