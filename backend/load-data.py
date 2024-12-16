from datetime import datetime
import sqlite3
import json

# Define the adapter for datetime to string
def adapt_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

# Define the converter from string to datetime
def convert_datetime(s):
    return datetime.strptime(s.decode(), "%Y-%m-%d %H:%M:%S")

# Register the adapter and converter
sqlite3.register_adapter(datetime, adapt_datetime)
sqlite3.register_converter("DATETIME", convert_datetime)

# Connect to the database with custom datetime handling
db = sqlite3.connect(
    "sqlite.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
)
cursor = db.cursor()

# Load station data
stations = json.load(open("data/stations.json"))

# Insert stations into the database
for station in stations:
    cursor.execute(
        '''
        INSERT OR IGNORE INTO station (id, number, name, lon, lat, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            station["id"],
            station["value_id"],
            station["name"],
            station["lon"],
            station["lat"],
            datetime.now(),
            datetime.now(),
        ),
    )

# Commit changes and close the connection
db.commit()
db.close()
