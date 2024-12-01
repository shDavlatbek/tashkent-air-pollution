<template>
  <div class="modal modal-blur fade" id="modal-alert" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-sm modal-dialog-centered" role="document">
      <div class="modal-content">
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        <div :class="['modal-status', `bg-${type}`]"></div>
        <div class="modal-body text-center py-4">
          <component :is="icons[type]" stroke="2" :class="['icon', 'mb-2', 'icon-lg', `text-${type}`]" />
          <h3>{{ props.title }}</h3>
          <div class="text-secondary" v-html="props.description"></div>
        </div>
        <div class="modal-footer">
          <div class="w-100">
            <div class="row">
              <slot name="buttons">
              </slot>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineExpose } from 'vue';
import { IconAlertCircle, IconCheck, IconInfoCircle } from '@tabler/icons-vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.min.js';

const icons = {
  danger: IconAlertCircle,
  success: IconCheck,
  info: IconInfoCircle
}

const props = defineProps({
  title: {
    type: String,
    default: 'Xatolik yuzaga keldi'
  },
  description: {
    type: String,
    default: null
  },
  type: {
    type: String,
    default: 'danger'
  }
})

const openModal = () => {
  const modalInstance = bootstrap.Modal.getOrCreateInstance('#modal-alert');
  modalInstance.show();
};

const closeModal = () => {
  const modalInstance = bootstrap.Modal.getOrCreateInstance('#modal-alert');
  modalInstance.hide();
};

// Expose methods to parent
defineExpose({
  openModal,
  closeModal,
});
</script>