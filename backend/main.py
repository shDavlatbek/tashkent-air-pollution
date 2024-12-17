from typing import AsyncIterator
from api.auth import fastapi_users
import uvicorn
from fastapi import Depends, FastAPI
from api.routers import all_routers
from starlette.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from contextlib import asynccontextmanager
from redis import asyncio as aioredis
from config import settings

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(settings.redis_url)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    
    
app = FastAPI(
    title="Unit Of Work & FastAPI Users", lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # "*" allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.post("/invalidate_cache")
async def invalidate_cache(
    user=Depends(fastapi_users.current_user(active=True))
):
    await FastAPICache.clear(namespace="fastapi-cache")
    return {"message": "Cache cleared"}


for router in all_routers:
    app.include_router(router)