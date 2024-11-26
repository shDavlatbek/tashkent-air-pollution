from fastapi import APIRouter

from api.dependencies import UOWDep
from services.common import RegionService, DistrictService


router = APIRouter(
    prefix="",
    tags=["Regions", "Districts"],
)


@router.get("/regions")
async def get_regions(
    uow: UOWDep,
):
    return await RegionService().get_regions(uow)


@router.get("/districts")
async def get_districts(
    uow: UOWDep,
    region_id: int = None
):
    return await DistrictService().get_districts(uow, region_id)