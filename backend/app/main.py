from fastapi import FastAPI

app = FastAPI(
    title="DataTrust API",
    version="0.1.0",
    description="Data preparation and analytics workspace API",
)

@app.get("/api/v1/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "datatrust-api"}
