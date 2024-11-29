from fastapi import APIRouter, Depends
from api.auth import fastapi_users

from api.dependencies import UOWDep
from services.common import RegionService, DistrictService


router = APIRouter(
    prefix="",
    tags=["Regions", "Districts"],
)


@router.get("/regions")
async def get_regions(
    uow: UOWDep,
    user=Depends(fastapi_users.current_user(active=True))
):
    return await RegionService().get_regions(uow)


@router.get("/districts")
async def get_districts(
    uow: UOWDep,
    region_id: int = None,
    user=Depends(fastapi_users.current_user(active=True))
):
    return await DistrictService().get_districts(uow, region_id)