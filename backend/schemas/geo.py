from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from schemas.common import CoordinateAdd


class AddGeoWell(BaseModel):
    number: int
    region: Optional[int]
    district: Optional[int]
    address: Optional[str]
    well_type: Optional[int]
    organization: Optional[int]
    location: Optional[int]
    station: Optional[int]
    coordinate: CoordinateAdd
    

class GeoWell(BaseModel):
    id: int
    number: int
    region: Optional[int] = None
    district: Optional[int] = None
    organization: Optional[int] = None
    station: Optional[int] = None
    location: Optional[int] = None
    well_type: Optional[int] = None
    coordinate: Optional[int] = None
    address: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True