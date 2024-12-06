from schemas.common import CoordinateAdd, NameFieldAdd
from schemas.geo import AddGeoWell, Parameter
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
                latitude_degree=well.coordinate.latitude_degree,
                latitude_minute=well.coordinate.latitude_minute,
                latitude_second=well.coordinate.latitude_second,
                longitude_degree=well.coordinate.longitude_degree,
                longitude_minute=well.coordinate.longitude_minute,
                longitude_second=well.coordinate.longitude_second,
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
            return await uow.geo_well.find_all()
        
    async def get_well(self, uow: IUnitOfWork, well_id: int):
        async with uow:
            well = await uow.geo_well.find_one(id=well_id)
            if well:
                well.coordinate = await uow.coordinate.find_one(id=well.coordinate)
                well.station = await uow.geo_station.find_one(id=well.station) if well.station else None
                well.organization = await uow.geo_organization.find_one(id=well.organization) if well.organization else None
                well.region = await uow.regions.find_one(id=well.region) if well.region else None
                well.district = await uow.districts.find_one(id=well.district) if well.district else None
                well.well_type = await uow.geo_well_type.find_one(id=well.well_type) if well.well_type else None
                well.location = await uow.location.find_one(id=well.location) if well.location else None
                return well
            else:
                return None
    
    async def edit_well(self, uow: IUnitOfWork, well_id: int, well: AddGeoWell):
        well_dict = well.model_dump()
        async with uow:
            await uow.geo_well.edit_one(well_id, well_dict)
            await uow.commit()
            
            
class ParameterNameService:
    async def add_parameter(self, uow: IUnitOfWork, parameter_name: NameFieldAdd):
        parameter_dict = parameter_name.model_dump()
        async with uow:
            parameter_id = await uow.parameter_name.add_one(parameter_dict)
            await uow.commit()
            return parameter_id
        
    async def get_parameters(self, uow: IUnitOfWork):
        async with uow:
            return await uow.parameter_name.find_all()

    
    async def edit_parameter(self, uow: IUnitOfWork, parameter_id: int, parameter_name: NameFieldAdd):
        parameter_name_dict = parameter_name.model_dump()
        async with uow:
            await uow.parameter_name.edit_one(parameter_id, parameter_name_dict)
            await uow.commit()
            

class ParameterService:
    async def add_parameter(self, uow: IUnitOfWork, parameter: Parameter):
        parameter_dict = parameter.model_dump()
        async with uow:
            parameter_id = await uow.parameter.add_one(parameter_dict)
            await uow.commit()
            return parameter_id
        
    async def get_parameters(self, uow: IUnitOfWork, filters):
        async with uow:
            if filters:
                return await uow.parameter.find_all(**filters)
            else:
                return await uow.parameter.find_all()

    
    async def edit_parameter(self, uow: IUnitOfWork, parameter_id: int, parameter: Parameter):
        parameter_dict = parameter.model_dump()
        async with uow:
            await uow.parameter.edit_one(parameter_id, parameter_dict)
            await uow.commit()