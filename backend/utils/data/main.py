import json
from request import download_file
from clean import clean_data

# Step 1: Download file
url = "https://opendata-back.tashkent.uz/oz/api/data/all/133/download?file_type=json"
downloaded_file = download_file(url, "data.json")

# Step 2: Load downloaded data
with open(downloaded_file, 'r') as file:
  data = json.load(file)
    
# Step 3: Define key and value mappings
key_map = {
  "Sana": "date",
  "Vaqt": "time",
  "Stansiya": "station",
  "AQI": "aqi",
  "Namlik": "hum",
  "Harorat": "temp",
  "Yog'ingarchilik": "prec",
  "PM2.5": "pm2.5"
}

value_map = {
  "station": {
    "G'afur G'ulom bog'i": "042112022",
    "Yangihayot tumani 329-maktab": "045112022",
    "Olmazor tumani, 423-bog'cha": "044112022",
    "Omazor tumani, Dermatalogiya": "043112022",
    "Yangi O'zbekiston Bog'i": "037112022",
    "Yangihayot tumani, 333-maktab": "038112022",
    "Lokomotiv Park": "041112022",
    "Tuzel-1 557-bog'cha": "039112022",
    "Bektemir tumani, 578-bog'cha": "040112022",
    "Xalqlar do'stligi": "036112022"
  }
}

# Step 4: Clean data
cleaned_data = clean_data(data, key_map, value_map)

# Step 5: Save processed data
with open("processed.json", 'w') as file:
  json.dump(cleaned_data, file, indent=4)