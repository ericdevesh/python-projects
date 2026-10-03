from dataclasses import dataclass

@dataclass(frozen=True)
class TradingCosts:
    """Research-only execution cost assumptions in price units."""
    spread: float = 0.00010
    slippage: float = 0.00002
    commission_r: float = 0.0

    def entry_price(self, side: str, raw_price: float) -> float:
        half = self.spread / 2.0
        slip = self.slippage
        return raw_price + half + slip if side == "BUY" else raw_price - half - slip

    def exit_price(self, side: str, raw_price: float) -> float:
        half = self.spread / 2.0
        slip = self.slippage
        return raw_price - half - slip if side == "BUY" else raw_price + half + slip

    def apply_commission(self, pnl_r: float) -> float:
        return pnl_r - self.commission_r
