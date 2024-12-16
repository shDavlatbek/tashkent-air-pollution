from schemas.station import ParameterSchema, ParameterUpdate
from utils.unitofwork import IUnitOfWork


class StationService:
    async def get_stations(self, uow: IUnitOfWork):
        async with uow:
            return await uow.geo_well.find_all()
        
    async def get_station(self, uow: IUnitOfWork, station_id: int):
        async with uow:
            station = await uow.station.find_one(id=station_id)
            if station:
                return station
            else:
                return None
    

class ParameterService:
    async def add_parameter(self, uow: IUnitOfWork, parameter: ParameterSchema):
        parameter_dict = parameter.model_dump()
        async with uow:
            parameter_id = await uow.parameter.add_one(parameter_dict)
            await uow.commit()
            return parameter_id
        
    async def get_parameters(self, uow: IUnitOfWork, filters):
        async with uow:
            start_date = filters.start_date
            end_date = filters.end_date
            filter_by = filters.model_dump(exclude={"start_date", "end_date"}, exclude_none=True)

            return await uow.parameter.find_all_with_dates(start_date=start_date, end_date=end_date, **filter_by)
    
    async def edit_parameter(self, uow: IUnitOfWork, parameter_id: int, parameter: ParameterUpdate):
        parameter_dict = parameter.model_dump()
        async with uow:
            await uow.parameter.edit_one(parameter_id, parameter_dict)
            await uow.commit()