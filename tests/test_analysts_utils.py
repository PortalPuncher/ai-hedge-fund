from src.utils import analysts


def test_get_analyst_nodes_keys():
    nodes = analysts.get_analyst_nodes()
    assert "ben_graham" in nodes
    node_name, func = nodes["ben_graham"]
    assert node_name == "ben_graham_agent"
    assert callable(func)


def test_get_agents_list_sorted():
    agents_list = analysts.get_agents_list()
    orders = [a["order"] for a in agents_list]
    assert orders == sorted(orders)
    keys = [a["key"] for a in agents_list]
    assert set(keys) == set(analysts.ANALYST_CONFIG.keys())


def test_get_agents_by_investing_style():
    groups = analysts.get_agents_by_investing_style()
    assert "value_investing" in groups
    value_agents = [a["key"] for a in groups["value_investing"]]
    assert "ben_graham" in value_agents
    orders = [a["order"] for a in groups["value_investing"]]
    assert orders == sorted(orders)
