import sqlite3
import json

db = sqlite3.connect('sqlite.db')
cursor = db.cursor()

regions = json.load(open('data/regions.json'))
districts = json.load(open('data/districts.json'))
locations = json.load(open('data/locations.json'))
geo_organizations = json.load(open('data/geo_organizations.json'))
geo_stations = json.load(open('data/geo_stations.json'))
geo_well_types = json.load(open('data/geo_well_types.json'))

for region in regions:
    cursor.execute(
        'INSERT OR IGNORE INTO region (id, name) VALUES (?, ?)',
        (region['id'], region['name_uz'])
    )
  
for district in districts:
    cursor.execute(
        'INSERT OR IGNORE INTO district (id, name, region_id) VALUES (?, ?, ?)',
        (district['id'], district['name_uz'], district['region_id'])
    )

for location in locations:
    cursor.execute(
        'INSERT OR IGNORE INTO location (id, name) VALUES (?, ?)',
        (location['id'], location['name'])
    )
    
for geo_organization in geo_organizations:
    cursor.execute(
        'INSERT OR IGNORE INTO geo_organization (id, name) VALUES (?, ?)',
        (geo_organization['id'], geo_organization['name'])
    )
    
for geo_station in geo_stations:
    cursor.execute(
        'INSERT OR IGNORE INTO geo_station (id, name) VALUES (?, ?)',
        (geo_station['id'], geo_station['name'])
    )

for geo_well_type in geo_well_types:
    cursor.execute(
        'INSERT OR IGNORE INTO geo_welltype (id, name) VALUES (?, ?)',
        (geo_well_type['id'], geo_well_type['name'])
    )

db.commit()
db.close()