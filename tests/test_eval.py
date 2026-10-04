from fastapi.testclient import TestClient
from ragevalx.main import app
client = TestClient(app)
GOLD = "The platform refuses latest tags."
CTX = "The platform refuses latest tags in production."

def test_pass_fail_and_trace():
    good = client.post("/evaluate", json={"answer": GOLD, "gold": GOLD, "contexts": [CTX], "latency_ms": 12, "cost_usd": 0.01}).json()
    assert good["passed"] is True and good["trace_id"]
    bad = client.post("/evaluate", json={"answer": "Soup is served", "gold": GOLD, "contexts": [CTX]}).json()
    assert bad["passed"] is False
