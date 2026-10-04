import re, time
STOP = set("the a an is of and to in".split())

def words(t):
    return set(re.findall(r"[a-z0-9]+", (t or "").lower())) - STOP

def evaluate(answer, gold, contexts, latency_ms=10, cost_usd=0.0):
    aw, gw = words(answer), words(gold)
    cw = set().union(*(words(c) for c in (contexts if isinstance(contexts, list) else [contexts or ""])))
    faith = len(aw & cw) / len(aw) if aw else 0
    rel = len(aw & gw) / len(gw) if gw else 0
    precision = (1.0 if contexts and len(words(contexts[0] if isinstance(contexts, list) else contexts) & gw) >= max(1, len(gw)//2) else 0.0)
    return {
        "faithfulness": round(faith, 4),
        "answer_relevance": round(rel, 4),
        "context_precision": precision,
        "latency_ms": latency_ms,
        "cost_usd": cost_usd,
        "passed": faith >= 0.5 and rel >= 0.5,
        "trace_id": "tr-local",
    }
