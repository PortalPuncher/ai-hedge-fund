import json
from unittest.mock import patch

from src.agents import risk_manager
from src.data.models import Price

class DummyILoc:
    def __init__(self, val):
        self.val = val
    def __getitem__(self, idx):
        return self.val

class DummySeries:
    def __init__(self, val):
        self.iloc = DummyILoc(val)
    def __getitem__(self, idx):
        return self.iloc[idx]

class DummyDF:
    def __init__(self, close_val):
        self.data = {"close": DummySeries(close_val)}
    @property
    def empty(self):
        return False
    def __getitem__(self, key):
        return self.data[key]



def test_risk_management_position_limits():
    state = {
        "messages": [],
        "data": {
            "portfolio": {"cash": 1000, "positions": {}},
            "tickers": ["AAPL"],
            "start_date": "2024-01-01",
            "end_date": "2024-01-02",
            "analyst_signals": {},
        },
        "metadata": {"show_reasoning": False},
    }

    dummy_price = Price(open=10, close=50, high=55, low=9, volume=100, time="2024-01-01T00:00:00Z")

    with patch("src.agents.risk_manager.get_prices", return_value=[dummy_price]), \
         patch("src.agents.risk_manager.prices_to_df", return_value=DummyDF(50)), \
         patch("src.agents.risk_manager.progress.update_status"):
        new_state = risk_manager.risk_management_agent(state)

    result = new_state["data"]["analyst_signals"]["risk_management_agent"]["AAPL"]
    assert result["remaining_position_limit"] == 200
    assert result["current_price"] == 50

    msg = new_state["messages"][-1]
    parsed = json.loads(msg.content)
    assert parsed["AAPL"]["remaining_position_limit"] == 200
