import argparse
import pandas as pd

from .backtest import run_backtest
from .report import print_report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--reward-risk", type=float, default=2.0)
    parser.add_argument("--stop-atr", type=float, default=1.0)
    args = parser.parse_args()

    df = pd.read_csv(args.file)
    df["time"] = pd.to_datetime(df["time"], utc=True)

    result = run_backtest(
        df,
        stop_atr=args.stop_atr,
        reward_risk=args.reward_risk,
    )
    print_report(result)


if __name__ == "__main__":
    main()
