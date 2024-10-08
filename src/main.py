from fastapi import FastAPI
from .database.models.endpoints import router

app = FastAPI()

app.include_router(router)