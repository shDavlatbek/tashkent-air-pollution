<template>
  <div class="card w-full">
    <div class="card-header flex flex-row items-center justify-between pb-2">
      <h2 class="card-title text-lg font-medium">Air Quality Index</h2>
      <div :class="`px-2 py-1 rounded-full ${getStatusColor(status)} text-white text-sm`">
        {{ status }}
      </div>
    </div>
    <div class="card-content">
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <span class="text-3xl font-bold">{{ aqi }}</span>
          <svg class="h-5 w-5 text-muted-foreground" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10" />
            <line x1="12" y1="8" x2="12" y2="12" />
            <line x1="12" y1="16" x2="12.01" y2="16" />
          </svg>
        </div>
        <div class="progress h-2" :style="{ width: progressValue + '%' }"></div>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <p class="text-sm font-medium">PM2.5</p>
            <p class="text-2xl font-bold">{{ pm25 }} µg/m³</p>
          </div>
          <div>
            <p class="text-sm font-medium">Updated</p>
            <p class="text-sm text-muted-foreground">{{ updatedTime }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';

export default {
  name: 'AirQualityCard',
  props: {
    aqi: {
      type: Number,
      required: true,
    },
    pm25: {
      type: Number,
      required: true,
    },
    status: {
      type: String,
      required: true,
      validator: (value) => ['Good', 'Moderate', 'Unhealthy', 'Very Unhealthy', 'Hazardous'].includes(value),
    },
  },
  setup(props) {
    const updatedTime = ref(new Date().toLocaleTimeString());

    const progressValue = computed(() => (props.aqi / 500) * 100);

    const getStatusColor = (status) => {
      const colors = {
        Good: 'bg-green-500',
        Moderate: 'bg-yellow-500',
        Unhealthy: 'bg-orange-500',
        'Very Unhealthy': 'bg-red-500',
        Hazardous: 'bg-purple-500',
      };
      return colors[status] || 'bg-gray-500';
    };

    return {
      updatedTime,
      progressValue,
      getStatusColor,
    };
  },
};
</script>

<style scoped>
.card {
  border: 1px solid #e5e7eb;
  border-radius: 0.375rem;
  background-color: #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  padding: 1rem;
}

.card-header {
  margin-bottom: 1rem;
}

.card-title {
  font-size: 1.25rem;
  font-weight: 600;
}

.card-content {
  padding: 1rem 0;
}

.progress {
  background-color: #d1d5db;
  height: 0.5rem;
  border-radius: 0.375rem;
}
</style>
