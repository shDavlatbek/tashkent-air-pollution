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
  return '#9168A1';
};

const updateMarkers = () => {
  if (map) {
    // Clear existing layers
    map.eachLayer((layer) => {
      if (layer instanceof L.Marker) {
        map.removeLayer(layer);
      }
    });

    // Add station markers
    props.stations.forEach(station => {
      const markerHtml = `
        <div class="station-marker" style="background-color: ${getAqiColor(station.aqi)}">
          <span>${station.aqi}</span>
        </div>
      `;

      const icon = L.divIcon({
        html: markerHtml,
        className: 'custom-div-icon',
        iconSize: [30, 30],
      });

      L.marker([station.lat, station.lng], { icon })
        .bindPopup(`
          <strong>${station.name}</strong><br>
          AQI: ${station.aqi}
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
