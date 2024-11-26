<template>
  <select v-model="localRegion" @change="updateRegion">
    <option v-for="region in regions" :key="region.id" :value="region.id">
      {{ region.name }}
    </option>
  </select>
</template>

<script>
export default {
  data() {
    return {
      localRegion: this.value, // Local model bound to v-model in parent
    };
  },
  props: {
    value: { // Accepts the selected region ID from the parent
      type: [Number, String],
      default: null
    },
    regions: {
      type: Object,
      default: () => {}
    }
  },
  methods: {
    updateRegion() {
      this.$emit('input', this.localRegion); // Emits the selected region to the parent
    }
  }
};
</script>
