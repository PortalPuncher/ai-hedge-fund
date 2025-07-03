def create_portfolio(initial_cash: float, margin_requirement: float, tickers: list[str]) -> dict:
    return {
        "cash": initial_cash,  # Initial cash amount
        "margin_requirement": margin_requirement,  # Initial margin requirement
        "margin_used": 0.0,  # total margin usage across all short positions
        "positions": {
            ticker: {
                "long": 0,  # Number of shares held long
                "short": 0,  # Number of shares held short
                "long_cost_basis": 0.0,  # Average cost basis for long positions
                "short_cost_basis": 0.0,  # Average price at which shares were sold short
                "short_margin_used": 0.0,  # Dollars of margin used for this ticker's short
            }
            for ticker in tickers
        },
        "realized_gains": {
            ticker: {
                "long": 0.0,  # Realized gains from long positions
                "short": 0.0,  # Realized gains from short positions
            }
            for ticker in tickers
        },
    }


def generate_portfolio_metrics(start_date: str, end_date: str) -> list[dict]:
    """Generate simple mock time-series metrics for demonstration."""
    from datetime import datetime, timedelta

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    days = (end - start).days

    metrics = []
    value = 100000.0
    for i in range(days + 1):
        current = start + timedelta(days=i)
        value += 1000 * ((-1) ** i)
        metrics.append(
            {
                "date": current.strftime("%Y-%m-%d"),
                "portfolio_value": value,
                "long_exposure": max(value * 0.6, 0),
                "short_exposure": max(value * 0.4, 0),
            }
        )
    return metrics
