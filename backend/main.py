from fastapi import FastAPI
from routes.generate import router

app = FastAPI(title="TRENDR-AI")

app.include_router(router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "alive"}