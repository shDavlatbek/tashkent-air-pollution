from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
    
    
class StationSchema(BaseModel):
    id: int
    number: int
    name: str
    lon: float
    lat: float
    created_at: datetime
    updated_at: datetime
    parameters: Optional[List['ParameterSchema']] = None  # Add this field

    class Config:
        from_attributes = True
        
        
class StationQuery(BaseModel):             
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    class Config:
        from_attributes = True
       
        
class ParameterAdd(BaseModel):
    station: int
    date_time: Optional[datetime] = Field(None, alias="datetime")
    aqi: Optional[float] = None
    hum: Optional[float] = None
    prec: Optional[float] = None
    pm25: Optional[float] = None

    class Config:
        from_attributes = True        
        
    
class ParameterSchema(ParameterAdd):
    id: int


class ParameterUpdate(ParameterAdd):
    station: Optional[int] = None 


class ParameterQuery(BaseModel):
    id: Optional[int] = None
    station: Optional[str] = None            
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    class Config:
        from_attributes = True