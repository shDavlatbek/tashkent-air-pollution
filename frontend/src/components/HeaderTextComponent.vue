<template>
  <div class="page-header d-print-none">
    <div class="container-xl">
      <div class="row g-2 align-items-center">
        <div class="col">
          <h2 class="page-title">
            {{ title }}
          </h2>
        </div>
        <div class="col-auto ms-auto d-print-none" v-if="modalId">
          <div class="btn-list">
            <a href="javascript:void(0)" class="btn btn-primary d-none d-sm-inline-block" data-bs-toggle="modal"
              :data-bs-target="'#'+modalId"
              @click="onModalOpen">
              <IconPlus class="icon" stroke="2" />
              Qo'shish
            </a>
            <a href="javascript:void(0)" class="btn btn-primary d-sm-none btn-icon" data-bs-toggle="modal" 
              :data-bs-target="'#'+modalId"
              aria-label="Qo'shish"
              @click="onModalOpen">
              <IconPlus class="icon" stroke="2" />
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { IconPlus } from '@tabler/icons-vue';


export default {
  name: 'HeaderText',
  props: {
    title: {
      type: String,
      required: true
    },
    modalId: {
      type: String,
      required: false
    },
    onModalOpen: {
      type: Function,
      required: false
    }
  },
  components: {
    IconPlus
  }
}

</script>