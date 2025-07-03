from app.backend.services.portfolio import generate_portfolio_metrics


def test_generate_portfolio_metrics():
    metrics = generate_portfolio_metrics("2024-01-01", "2024-01-05")
    assert len(metrics) == 5
    first = metrics[0]
    assert first["date"] == "2024-01-01"
    assert "portfolio_value" in first
