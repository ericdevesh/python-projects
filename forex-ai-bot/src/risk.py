def position_size(
    balance: float,
    risk_fraction: float,
    stop_distance_price: float,
    value_per_price_unit: float,
) -> float:
    """Generic risk-based sizing.

    value_per_price_unit must be supplied for the specific broker/symbol contract.
    This avoids silently assuming pip/tick value conventions.
    """
    if balance <= 0 or risk_fraction <= 0:
        return 0.0
    if stop_distance_price <= 0 or value_per_price_unit <= 0:
        return 0.0

    risk_amount = balance * risk_fraction
    return risk_amount / (stop_distance_price * value_per_price_unit)
