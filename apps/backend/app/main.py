from fastapi import FastAPI
from app.api.v1.root import router as api_router

app = FastAPI(
    title="Guia de Bares SP API",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")