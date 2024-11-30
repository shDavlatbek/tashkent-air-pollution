from datetime import datetime
from sqlalchemy import Boolean, ForeignKey, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.common import NameField
from schemas.geo import GeoWell


class Organization(Base):
    __tablename__ = "geo_organization"
    pydantic_model = NameField
    name: Mapped[str] = mapped_column(String(length=150), nullable=False)
    

class Station(Base):
    __tablename__ = "geo_station"
    pydantic_model = NameField
    name: Mapped[str] = mapped_column(String(length=150), nullable=False)
  

class WellType(Base):
    __tablename__ = "geo_welltype"
    pydantic_model = NameField
    name: Mapped[str] = mapped_column(String(length=150), nullable=False)


class GeoWell(Base):
    __tablename__ = "geo_well"
    pydantic_model = GeoWell
    number: Mapped[int] = mapped_column(nullable=False)
    region: Mapped[int] = mapped_column(ForeignKey('region.id'), nullable=True)
    district: Mapped[int] = mapped_column(ForeignKey('district.id'), nullable=True)
    organization: Mapped[int] = mapped_column(ForeignKey('geo_organization.id'), nullable=True)
    station: Mapped[int] = mapped_column(ForeignKey('geo_station.id'), nullable=True)
    location: Mapped[int] = mapped_column(ForeignKey('location.id'), nullable=True)
    well_type: Mapped[int] = mapped_column(ForeignKey('geo_welltype.id'), nullable=True)
    coordinate: Mapped[int] = mapped_column(ForeignKey('coordinate.id'), nullable=True)
    address: Mapped[str] = mapped_column(String(length=250), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        nullable=False, 
        default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        nullable=False, 
        onupdate=func.now(), 
        default=func.now()
    )