import asyncio
from datetime import datetime
import asyncpg
import json
from config import settings

# Database configuration
DATABASE_URL = settings.database_url_notasync

# Load JSON data
stations = json.load(open("data/stations.json"))
parameters = json.load(open("data/parameters.json"))

async def insert_data():
    # Connect to the PostgreSQL database
    conn = await asyncpg.connect(DATABASE_URL)

    try:
        # Insert parameter data
        for station in stations:
            await conn.execute(
                '''
                INSERT INTO station (id, number, name, lon, lat, created_at, updated_at)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
                ''',
                station["id"],
                station["value_id"],
                station["name"],
                station["lon"],
                station["lat"],
                datetime.now(),
                datetime.now()
            )

        
        for parameter in parameters:
            await conn.execute(
                '''
                INSERT INTO parameter (station, datetime, aqi, hum, prec, pm25)
                VALUES ($1, $2, $3, $4, $5, $6)
                ''',
                parameter["station"],
                datetime.strptime(f"{parameter['date']} {parameter['time']}", "%Y-%m-%d %H:%M:%S"),
                parameter["aqi"],
                parameter["hum"],
                parameter["prec"],
                parameter["pm2.5"]
            )

        # Insert station data
        
    finally:
        # Close the connection
        await conn.close()

# Run the script
asyncio.run(insert_data())