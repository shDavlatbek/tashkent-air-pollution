from datetime import datetime
from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from schemas.station import StationSchema, ParameterSchema


class Station(Base):
    __tablename__ = "station"
    pydantic_model = StationSchema
    number: Mapped[str] = mapped_column(String(length=250), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(length=250), nullable=False)
    lon: Mapped[float] = mapped_column(nullable=False)
    lat: Mapped[float] = mapped_column(nullable=False)
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
    parameters: Mapped[list["Parameter"]] = relationship("Parameter", back_populates="station_obj")
    

class Parameter(Base):
    __tablename__ = "parameter"
    pydantic_model = ParameterSchema
    station: Mapped[int] = mapped_column(ForeignKey('station.number'), nullable=False)
    datetime: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    aqi: Mapped[float] = mapped_column(nullable=True)
    hum: Mapped[float] = mapped_column(nullable=True)
    prec: Mapped[float] = mapped_column(nullable=True)
    pm25: Mapped[float] = mapped_column(nullable=True)
    station_obj: Mapped["Station"] = relationship("Station", back_populates="parameters")