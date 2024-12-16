from typing import Optional
from pydantic import BaseModel
from datetime import datetime
    
    
class StationSchema(BaseModel):
    id: int
    number: int
    name: str
    lon: float
    lat: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        
        
class ParameterAdd(BaseModel):
    station: int
    datetime: Optional[datetime] = None
    aqi: Optional[int] = None
    hum: Optional[int] = None
    prec: Optional[int] = None
    pm25: Optional[int] = None

    class Config:
        from_attributes = True        
        
    
class ParameterSchema(ParameterAdd):
    id: int


class ParameterUpdate(ParameterAdd):
    station: Optional[int] = None 


class ParameterQuery(BaseModel):
    id: Optional[int] = None
    station: Optional[str] = None
    parameter: Optional[str] = None               
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    class Config:
        from_attributes = True