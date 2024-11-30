from typing import Optional
from pydantic import Field, BaseModel


class Region(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class District(BaseModel):
    id: int
    name: str
    region_id: int

    class Config:
        from_attributes = True
        
        
class  NameField(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
        

class CoordinateAdd(BaseModel):
    latitude_degree: Optional[float]
    latitude_minute: Optional[float]
    latitude_second: Optional[float]
    longitude_degree: Optional[float]
    longitude_minute: Optional[float]
    longitude_second: Optional[float]
    x: Optional[float]
    y: Optional[float]
    
    class Config:
        from_attributes = True
        

class Coordinate(CoordinateAdd):
    id: int

    class Config:
        from_attributes = True