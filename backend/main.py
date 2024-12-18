from api.auth import fastapi_users
from fastapi import Depends, FastAPI
from api.routers import all_routers
from starlette.middleware.cors import CORSMiddleware
from utils.filldb import fetch_and_fill_data_async
from api.dependencies import UOWDep


app = FastAPI(
    title="Unit Of Work & FastAPI Users",
    root_path="/api/v1"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", 'http://air.georesearch.uz'],  # "*" allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/fetch-data")
async def manual_fetch_data(uow: UOWDep, user=Depends(fastapi_users.current_user(active=True))):
    await fetch_and_fill_data_async(uow)
    return {"message": "Data fetched and filled successfully"}


for router in all_routers:
    app.include_router(router)