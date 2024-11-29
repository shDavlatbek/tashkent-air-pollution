<template>
  <div class="modal modal-blur fade" id="modal-danger" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-sm modal-dialog-centered" role="document">
      <div class="modal-content">
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        <div class="modal-status bg-danger"></div>
        <div class="modal-body text-center py-4">
          <IconAlertTriangle stroke="2" class="icon mb-2 text-danger icon-lg" />
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
import { IconAlertTriangle } from '@tabler/icons-vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.min.js';

const props = defineProps({
  title: {
    type: String,
    default: 'Xatolik yuzaga keldi'
  },
  description: {
    type: String,
    default: null
  }
})

const openModal = () => {
  const modalInstance = bootstrap.Modal.getOrCreateInstance('#modal-danger');
  modalInstance.show();
};

const closeModal = () => {
  const modalInstance = bootstrap.Modal.getOrCreateInstance('#modal-danger');
  modalInstance.hide();
};

// Expose methods to parent
defineExpose({
  openModal,
  closeModal,
});
</script>