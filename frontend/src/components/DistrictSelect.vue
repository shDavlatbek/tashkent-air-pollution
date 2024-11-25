<template>
  <select v-model="localDistrict" @change="updateDistrict">
    <option value>---------</option>
    <option v-for="district in districts" :key="district.id" :value="district.id">
      {{ district.name }}
    </option>
  </select>
</template>

<script>
export default {
  props: {
    regionId: { // The selected region ID passed from parent
      type: [Number, String],
      required: true
    },
    value: { // The selected district ID passed from parent
      type: [Number, String],
      default: null
    },
    districts: { // The list of districts passed from parent
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      localDistrict: this.value, // Local model for district
    };
  },
  methods: {
    updateDistrict() {
      this.$emit('input', this.localDistrict); // Emit selected district to parent
    }
  },
};
</script>
