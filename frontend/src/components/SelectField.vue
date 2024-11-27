<template>
  <div :class="'mb-'+props.margin">
    <label v-if="props.label" :class="{'form-label':true, 'required': props.required}">{{ props.label }}</label>
    <select 
      class="form-select"
      :required="props.required"
      :disabled="props.disabled"
      v-bind="attrs"
      v-model="model"
      v-on="$attrs"
    >
      <option v-if="!props.required" :value="emptyValue">{{ emptyText }}</option>
      <slot></slot>
    </select>
  </div>
</template>

<script setup>
import { defineModel, defineProps } from 'vue'
const model = defineModel()
const props = defineProps({
  value: {
    type: [String, Number],
    default: null
  },
  label: {
    type: String,
    default: null,
  },
  required: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  margin: {
    type: [String, Number],
    default: '3'
  },
  emptyValue: {
    type: [String, Number],
    default: null
  },
  emptyText: {
    type: String,
    default: '---------'
  },
  attrs: {
    type: Object,
    default: () => ({})
  }
})
</script>