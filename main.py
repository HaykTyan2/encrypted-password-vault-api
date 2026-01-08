from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.api.health import router as health_router
from src.api.auth import router as auth_router
from src.api.entries import router as entries_router
from src.database.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(">>> INIT_DB CALLED <<<")
    init_db()
    yield


app = FastAPI(
    title="Password Vault Backend",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(entries_router)




# PREVIOUS VRSION BEFORE app.include_router(....)
# when someone makes an HTTP GET request to /health, run the function below
# @app.get("/health")
# @app.get() auto registers the function below it as the handler for that route.
# the function returns a dict {} and FastAPI converts it to a JSON and UVICORN sends that JSON response back
# JSON is what the "internet" understands and since a DICT is the closest representation of JSON we must return a DICT
# def health_check():
#   return {"status": "ok"}