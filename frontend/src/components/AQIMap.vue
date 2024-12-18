<script setup>
import { onMounted, ref, watch, defineProps } from 'vue';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

const mapContainer = ref(null);
let map;

const props = defineProps({
  stations: {
    type: Array,
    required: true,
    default: () => []
  }
});

const getAqiColor = (aqi) => {

  
  if (aqi <= 50) return '#00e400';
  if (aqi <= 100) return '#f7D543';
  if (aqi <= 150) return '#ff7e00';
  if (aqi <= 200) return '#E95F5E';
  if (aqi <= 300) return '#9168A1';
  
  return '#9D6878';
};

function utcRoundedTime (){
      const now = new Date();
      return new Date(Date.UTC(
        now.getUTCFullYear(),
        now.getUTCMonth(),
        now.getUTCDate(),
        now.getUTCHours(), // Keep hours
        0,                 // Set minutes to 0
        0,                 // Set seconds to 0
        0                  // Set milliseconds to 0
      ));
    }

function getCurTimeParameter(parameters){
  const curTime = utcRoundedTime();
  const curTimeParameter = parameters.find((param) => {
    const paramTime = new Date(param.datetime);
    return paramTime.getTime() === curTime.getTime();
  });
  console.log(curTimeParameter);
  
  return curTimeParameter;
}

const updateMarkers = () => {
  if (map) {
    // Clear existing layers
    map.eachLayer((layer) => {
      if (layer instanceof L.Marker || layer instanceof L.Circle) {
        map.removeLayer(layer);
      }
    });

    // Add station markers and circles
    props.stations.forEach(station => {
      // getAqiColor(station?.parameter[0]?.aqi)
      // station?.parameter[0]?.aqi
      let markerHtml
      if (getCurTimeParameter(station?.parameters)){
        markerHtml = `
          <div class="station-marker" style="background-color: ${getAqiColor(station?.parameters[0]?.aqi)}">
            <span>${station?.parameters[0]?.aqi}</span>
          </div>
        `;

      }else{
        markerHtml = `
          <div class="station-marker" style="background-color: ${"transparent"}">
            <span>Sensor mavjud emas</span>
          </div>
        `;
      }
      
      const icon = L.divIcon({
        html: markerHtml,
        className: 'custom-div-icon',
        iconSize: [30, 30],
      });

      // Add circle with opacity
      L.circle([station.lat, station.lon], {
        color: getAqiColor(station?.parameters[0]?.aqi),
        fillColor: getAqiColor(station?.parameters[0]?.aqi),
        fillOpacity: 0.2,
        radius: 2000
      }).addTo(map);

      L.marker([station.lat, station.lon], { icon })
        .bindPopup(`
          <strong>${station?.name}</strong><br>
          AQI: ${station?.parameters[0]?.aqi}
        `)
        .addTo(map);
    });
  }
};

onMounted(() => {
  if (mapContainer.value) {
    // Initialize map
    map = L.map(mapContainer.value).setView([41.2995, 69.2401], 12);

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Initial marker load
    updateMarkers();
  }
});

watch(() => props.stations, updateMarkers, { deep: true });
</script>

<template>
  <div class="map-container">
    <div ref="mapContainer" class="map"></div>
    <div class="time-tracker">
      {{ new Date().toLocaleTimeString() }}
    </div>
  </div>
</template>

<style scoped>
.map-container {
  position: relative;
  width: 100%;
  height: 500px;
}

.map {
  width: 100%;
  height: 100%;
}

.time-tracker {
  position: absolute;
  top: 10px;
  right: 10px;
  background: white;
  padding: 5px 10px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  z-index: 1000;
}

:deep(.station-marker) {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  box-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

:deep(.custom-div-icon) {
  background: none;
  border: none;
}
</style>
