from fastapi import APIRouter, Depends
from api.auth import fastapi_users

from api.dependencies import UOWDep
from services.common import RegionService, DistrictService
from services.geo import ParameterNameService as PNService
from schemas.common import NameFieldAdd


router = APIRouter(
    prefix="",
    tags=["Regions, Districts, Parameter names"],
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


@router.get("/parameter-names")
async def  get_parameter_names(
    uow: UOWDep,
    user=Depends(fastapi_users.current_user(active=True))
):
    return await PNService().get_parameters(uow)


@router.post("/parameter-names/add")
async def  add_parameter_name(
    uow: UOWDep,
    parameter_name: NameFieldAdd,
    user=Depends(fastapi_users.current_user(active=True))
):
    return {"parameter_id": await PNService().add_parameter(uow, parameter_name)}


@router.post("/parameter-names/edit")
async def  edit_parameter_name(
    uow: UOWDep,
    parameter_id: int,
    parameter_name: NameFieldAdd,
    user=Depends(fastapi_users.current_user(active=True))
):  
    await PNService().edit_parameter(uow, parameter_id, parameter_name)
    return {"ok": True}