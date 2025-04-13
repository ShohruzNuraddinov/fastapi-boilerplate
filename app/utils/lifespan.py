from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.utils.db import init_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler for the FastAPI application.
    This function is called when the application starts and stops.
    """
    await init_db()
    yield
    await close_db()
    # Code to run when the application stops