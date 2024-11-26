# You can define your repositories here

from models.common import Region, District
from utils.repository import SQLAlchemyRepository


class RegionRepository(SQLAlchemyRepository):
    model = Region

class DistrictRepository(SQLAlchemyRepository):
    model = District