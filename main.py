from fastapi import FastAPI
from backend.app.api.drift import router as drift_router

app = FastAPI()

app.include_router(drift_router)