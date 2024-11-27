<template>
  <div :class="'mb-'+props.margin">
    <slot name="before-label"></slot>
    <label v-if="props.label" :class="{'form-label':true, 'required': props.required}">{{ props.label }}</label>
    <slot name="before"></slot>
    <input
      class="form-control"
      :type="props.type"
      :placeholder="props.placeholder"
      :required="props.required"
      :disabled="props.disabled"
      v-bind="attrs"
      v-model="model"
      v-on="$attrs"
    >
    <slot name="after"></slot>
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
    default: null
  },
  placeholder: {
    type: String,
    default: null
  },
  type: {
    type: String,
    default: "text"
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
  attrs: {
    type: Object,
    default: () => ({})
  }
})
</script>