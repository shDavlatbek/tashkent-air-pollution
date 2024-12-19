from datetime import datetime, timedelta, timezone
import json
from api.dependencies import UOWDep
from services.station import StationService, ParameterService
from schemas.station import ParameterAdd, ParameterQuery
from pydantic_settings import BaseSettings
from utils.common import now_utc_hours, now_hours
import aiohttp
import asyncio
import pytz

from utils.unitofwork import UnitOfWork, get_uow

class Settings(BaseSettings):
    api_url: str
    login: str
    password: str

    class Config:
        env_file = ".env_air"
        env_file_encoding = "utf-8"
        env_file_priority = True

settings = Settings()

API_URL = settings.api_url
USERNAME = settings.login
PASSWORD = settings.password
PARAMETERS = ["aqi", "humidity", "rain", "pm2_5"]
STATIONS = {"036112022", "037112022", "038112022", "039112022", "040112022",
            "041112022", "042112022", "043112022", "044112022", "045112022"}

tz=pytz.timezone("Asia/Tashkent")

async def fetch_and_fill_data(uow: UOWDep):
    return await StationService().get_station(uow)

async def fetch_parameter_data(session: aiohttp.ClientSession, parameter, start_date: datetime, end_date):
    headers = {
        "Content-Type": "application/json",
    }
    
    payload = {
        "start_date": start_date.isoformat(sep=' '),
        "end_date": end_date.isoformat(sep=' '),
        "parameter": parameter,
    }
    auth = aiohttp.BasicAuth(login=USERNAME, password=PASSWORD)

    async with session.post(API_URL, json=payload, auth=auth, headers=headers) as response:
        if response.status == 200:
            return await response.json()
        else:
            return response
        
        
async def fetch_and_fill_data_async(uow: UnitOfWork):
    async with aiohttp.ClientSession() as session:
        async with uow:
            last_record = (await ParameterService().get_parameters(uow, ParameterQuery(start_date=None, end_date=None), 1))[0]
            if last_record.date_time == now_utc_hours():
                return
            start_date = (last_record.date_time.astimezone(tz).replace(tzinfo=None) + timedelta(hours=1))
            end_date = now_hours()

            tasks = []
            for parameter in PARAMETERS:
                tasks.append(fetch_parameter_data(session, parameter, start_date, end_date))

            responses = await asyncio.gather(*tasks)
            
            merged_dict_by_id_time  = {}

            for parameter, sublist in zip(PARAMETERS, responses):
                stations = []
                for item in sublist['data']:
                    station_id = item["station_id"]
                    if station_id == "Average":
                        continue
                    stations.append(station_id)
                    date_time = item["datetime"]
                    
                    key = (station_id, date_time)
                    
                    if key not in merged_dict_by_id_time:
                        merged_dict_by_id_time[key] = item.copy()  
                    else:
                        merged_dict_by_id_time[key].update(item)


            merged_result = list(merged_dict_by_id_time.values())
            
            for parameter in merged_result:
                await ParameterService().add_parameter(uow, ParameterAdd(
                    station=parameter["station_id"],
                    datetime=parameter["datetime"],
                    aqi=parameter.get("aqi"),
                    hum=parameter.get("humidity"),
                    prec=parameter.get("rain"),
                    pm25=parameter.get("pm2_5")
                ))
            return merged_result