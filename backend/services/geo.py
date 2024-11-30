from schemas.common import CoordinateAdd
from schemas.geo import AddGeoWell
from utils.unitofwork import IUnitOfWork


class GeoService:
    async def add_well_form(self, uow: IUnitOfWork):
        async with uow:
            locations = await uow.location.find_all()
            organizations = await uow.geo_organization.find_all()
            well_types = await uow.geo_well_type.find_all()
            stations = await uow.geo_station.find_all()
            return {
                "locations": locations,
                "organizations": organizations,
                "well_types": well_types,
                "stations": stations
            }
    
    async def add_well(self, uow: IUnitOfWork, well: AddGeoWell):
        well_dict = well.model_dump()
        async with uow:
            coordinate = CoordinateAdd(
                latitude_degree=well.coordinate.latitude.degree,
                latitude_minute=well.coordinate.latitude.minute,
                latitude_second=well.coordinate.latitude.second,
                longitude_degree=well.coordinate.longitude.degree,
                longitude_minute=well.coordinate.longitude.minute,
                longitude_second=well.coordinate.longitude.second,
                x=well.coordinate.x,
                y=well.coordinate.y,
            ).model_dump()
            coordinate_id = await uow.coordinate.add_one(coordinate)
            well_dict['coordinate'] = coordinate_id
            well_id = await uow.geo_well.add_one(well_dict)
            await uow.commit()
            return well_id

    async def get_wells(self, uow: IUnitOfWork):
        async with uow:
            wells = await uow.geo_well.find_all()
            return wells
        
    async def get_well(self, uow: IUnitOfWork, well_id: int):
        async with uow:
            well = await uow.geo_well.find_one(id=well_id)
            well.coordinate = await uow.coordinate.find_one(id=well.coordinate)
            well.station = await uow.geo_station.find_one(id=well.station)
            well.organization = await uow.geo_organization.find_one(id=well.organization)
            well.region = await uow.regions.find_one(id=well.region)
            well.district = await uow.districts.find_one(id=well.district)
            well.well_type = await uow.geo_well_type.find_one(id=well.well_type)
            well.location = await uow.location.find_one(id=well.location)
            return well
    
    async def edit_well(self, uow: IUnitOfWork, well_id: int, well: AddGeoWell):
        well_dict = well.model_dump()
        async with uow:
            await uow.geo_well.edit_one(well_id, well_dict)
            await uow.commit()