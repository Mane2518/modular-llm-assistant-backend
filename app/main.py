from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(
    title="Modular LLM Assistant API",
    description="Backend for AI Assistant with Memory and LLM Integration",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the Modular LLM Assistant API"}
