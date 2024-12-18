from typing import List, Optional, Tuple
from pydantic import BaseModel, Field, model_validator
from datetime import datetime, timedelta, timezone

from utils.common import now_utc_hours
    
    
class StationSchema(BaseModel):
    id: int
    number: str
    name: str
    lon: float
    lat: float
    created_at: datetime
    updated_at: datetime
    parameters: Optional[List['ParameterSchema']] = None

    class Config:
        exclude_none = True
        from_attributes = True
        
        
class StationQuery(BaseModel):  
    station: Optional[str] = None           
    start_date: Optional[datetime] = now_utc_hours() - timedelta(days=10)
    end_date: Optional[datetime] = now_utc_hours()
    
    @property
    def datetime(self) -> Tuple[Optional[datetime], Optional[datetime]]:
        return (self.start_date, self.end_date)

    class Config:
        from_attributes = True

    def model_dump(self, **kwargs):
        if self.start_date is None and self.end_date is None:
            return []
        
        # Pass the 'exclude' parameter to remove 'start_date' and 'end_date' from the dump
        exclude = kwargs.get("exclude", [])
        exclude.extend(["start_date", "end_date"])
        
        # Now call the original model_dump method with the updated exclude fields
        data = super().model_dump(**kwargs, exclude=exclude)
        
        # Add the 'datetime' field as a tuple of (start_date, end_date)
        data["datetime"] = (self.start_date, self.end_date)
        
        return data
       
        
class ParameterAdd(BaseModel):
    station: str
    date_time: Optional[datetime] = Field(None, alias="datetime")
    aqi: Optional[float] = None
    hum: Optional[float] = None
    prec: Optional[float] = None
    pm25: Optional[float] = None

    class Config:
        from_attributes = True        
        
    def model_dump(self, **kwargs):
        
        # Pass the 'exclude' parameter to remove 'start_date' and 'end_date' from the dump
        exclude = kwargs.get("exclude", [])
        exclude.extend(["date_time"])
        
        # Now call the original model_dump method with the updated exclude fields
        data = super().model_dump(**kwargs, exclude=exclude)
        
        # Add the 'datetime' field as a tuple of (start_date, end_date)
        data["datetime"] = (self.date_time)
        
        return data
        
    
class ParameterSchema(ParameterAdd):
    id: int


class ParameterUpdate(ParameterAdd):
    station: Optional[str] = None 


class ParameterQuery(BaseModel):
    id: Optional[int] = None
    station: Optional[str] = None            
    start_date: Optional[datetime] = now_utc_hours() - timedelta(days=10) 
    end_date: Optional[datetime] = now_utc_hours()

    @property
    def datetime(self) -> Tuple[Optional[datetime], Optional[datetime]]:
        return (self.start_date, self.end_date)

    class Config:
        from_attributes = True

    def model_dump(self, **kwargs):
        
        if self.start_date is None and self.end_date is None:
            return []
        
        # Pass the 'exclude' parameter to remove 'start_date' and 'end_date' from the dump
        exclude = kwargs.get("exclude", [])
        exclude.extend(["start_date", "end_date"])
        
        # Now call the original model_dump method with the updated exclude fields
        data = super().model_dump(**kwargs, exclude=exclude)
        
        # Add the 'datetime' field as a tuple of (start_date, end_date)
        data["datetime"] = (self.start_date, self.end_date)
        
        return data