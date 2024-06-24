from contextlib import asynccontextmanager

import uvicorn
from typing import Annotated
from fastapi import FastAPI, Body, Path
from pydantic import EmailStr, BaseModel
from core.models import Base, db_helper

from items_views import router as items_router
from users.views import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
# app.include_router(items_router, prefix="/items-views") Можно так или
app.include_router(items_router)

app.include_router(user_router)


@app.get("/")
def return_index():
    return {"message": "Hello index"}


@app.get("/hello/")
def hello_name(name: str = "Anon"):
    name = name.strip().title()
    return {"hello": f"Hello {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
