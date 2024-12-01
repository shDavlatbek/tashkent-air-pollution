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
    latitude_degree: Optional[float] = None
    latitude_minute: Optional[float] = None
    latitude_second: Optional[float] = None
    longitude_degree: Optional[float] = None
    longitude_minute: Optional[float] = None
    longitude_second: Optional[float] = None
    x: Optional[float] = None
    y: Optional[float] = None
    
    class Config:
        from_attributes = True
        

class Coordinate(CoordinateAdd):
    id: int

    class Config:
        from_attributes = True