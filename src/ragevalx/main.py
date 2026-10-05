from ragevalx.ops import router as ops_router
from fastapi import FastAPI
from ragevalx.score import evaluate
app = FastAPI(title="RAG Evaluation Observability")
app.include_router(ops_router, prefix="/v1")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/evaluate")
def post_eval(body: dict):
    return evaluate(body.get("answer"), body.get("gold"), body.get("contexts", body.get("context")), body.get("latency_ms", 10), body.get("cost_usd", 0))
