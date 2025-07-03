import json
from unittest.mock import patch

from src.agents import portfolio_manager
from src.agents.portfolio_manager import PortfolioManagerOutput, PortfolioDecision


def test_portfolio_manager_trade_decision():
    state = {
        "messages": [],
        "data": {
            "portfolio": {"cash": 1000, "positions": {}},
            "tickers": ["AAPL"],
            "analyst_signals": {
                "risk_management_agent": {
                    "AAPL": {"remaining_position_limit": 500, "current_price": 50}
                }
            },
        },
        "metadata": {"show_reasoning": False},
    }

    pm_output = PortfolioManagerOutput(
        decisions={
            "AAPL": PortfolioDecision(action="buy", quantity=5, confidence=80.0, reasoning="ok")
        }
    )

    with patch("src.agents.portfolio_manager.call_llm", return_value=pm_output) as mock_llm, \
         patch("src.agents.portfolio_manager.progress.update_status"):
        new_state = portfolio_manager.portfolio_management_agent(state)

    mock_llm.assert_called_once()

    msg = new_state["messages"][-1]
    content = json.loads(msg.content)
    assert content["AAPL"]["action"] == "buy"
    assert content["AAPL"]["quantity"] == 5
