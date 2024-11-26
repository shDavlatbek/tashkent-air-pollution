import sqlite3
import json

db = sqlite3.connect('sqlite.db')
cursor = db.cursor()

regions = json.load(open('data/regions.json'))
districts = json.load(open('data/districts.json'))

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

db.commit()
db.close()