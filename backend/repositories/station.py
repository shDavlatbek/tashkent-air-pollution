from models.station import Station, Parameter
from utils.repository import SQLAlchemyRepository, SQLAlchemyRepositoryModified


class StationRepository(SQLAlchemyRepository):
    model = Station
    

class ParameterRepository(SQLAlchemyRepositoryModified):
    model = Parameter