from fastapi import APIRouter, Depends
from api.auth import fastapi_users

from api.dependencies import UOWDep
from services.geo import GeoService
from schemas.geo import AddGeoWell


router = APIRouter(
    prefix="/geo",
    tags=["Geo"],
)


@router.get("/add")
async def add_well_form(
    uow: UOWDep,
    user=Depends(fastapi_users.current_user(active=True))
):
    return await GeoService().add_well_form(uow)


@router.post("/add")
async def add_well(
    uow: UOWDep,
    well: AddGeoWell,
    user=Depends(fastapi_users.current_user(active=True))
):
    return await GeoService().add_well(uow, well)


@router.get("/")
async def get_wells(
    uow: UOWDep,
    user=Depends(fastapi_users.current_user(active=True))
):
    res = []
    wells = await GeoService().get_wells(uow)
    for well in wells:
        res.append(await GeoService().get_well(uow, well.id))
    return res


@router.get("/{id}")
async def get_well(
    uow: UOWDep,
    id: int,
    user=Depends(fastapi_users.current_user(active=True))
):
    return await GeoService().get_well(uow, id)