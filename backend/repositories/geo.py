from models.geo import GeoWell, WellType, Organization, Station
from utils.repository import SQLAlchemyRepository


class GeoWellRepository(SQLAlchemyRepository):
    model = GeoWell


class GeoWellTypeRepository(SQLAlchemyRepository):
    model = WellType


class GeoOrganizationRepository(SQLAlchemyRepository):
    model = Organization


class GeoStationRepository(SQLAlchemyRepository):
    model = Station