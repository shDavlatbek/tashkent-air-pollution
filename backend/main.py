from typing import AsyncIterator
import uvicorn
from fastapi import FastAPI
from api.routers import all_routers
from starlette.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.backends.memcached import MemcachedBackend
from contextlib import asynccontextmanager
# import aioredis
import argparse
import aiomcache

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    # redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(MemcachedBackend(aiomcache), prefix="fastapi-cache")
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


for router in all_routers:
    app.include_router(router)