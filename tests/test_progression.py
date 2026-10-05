from ragevalx.progression import rag_eval

def test_rag_eval_picks_winner():
    out = rag_eval("what is drift", [
        {"name": "a", "chunking": "fixed", "retrieval": "bm25", "context": "drift is distribution change", "answer": "drift is distribution change", "latency_ms": 12, "cost_usd": 0.0},
        {"name": "b", "chunking": "semantic", "retrieval": "vector", "context": "unrelated", "answer": "hello", "latency_ms": 40, "cost_usd": 0.02},
    ])
    assert out["chatbot_only"] is False
    assert out["winner"] == "a"

