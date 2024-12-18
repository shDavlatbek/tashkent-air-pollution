from models.station import Station, Parameter
from utils.repository import SQLAlchemyRepository


class StationRepository(SQLAlchemyRepository):
    model = Station
    

class ParameterRepository(SQLAlchemyRepository):
    model = Parameter