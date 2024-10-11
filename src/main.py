from fastapi import FastAPI
from src.endpoints.endpoints import router

app = FastAPI()

app.include_router(router)