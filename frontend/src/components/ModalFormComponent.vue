<template>
  <div class="modal modal-blur fade" :id="modalId" tabindex="-1" role="dialog">
    <div class="modal-dialog modal-xl modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ modalTitle }}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <form>
          <slot name="modal-body"></slot>
          <div class="modal-footer">
            <a href="javascript:void(0)" class="btn btn-link link-secondary" data-bs-dismiss="modal">
              Bekor qilish
            </a>
            <input type="reset" class="btn ms-auto" value="Tozalash" />
            <a href="javascript:void(0)" @click="modalFormConfirm" class="btn btn-primary" data-bs-dismiss="modal">
              <IconPlus class="icon" stroke="2" />
              Qo'shish
            </a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { IconPlus } from '@tabler/icons-vue';


export default {
  name: 'ModalForm',
  props: {
    modalId: {
      type: String,
      required: true
    },
    modalTitle: {
      type: String,
      required: true
    },
    modalFormConfirm: {
      type: Function,
      required: true
    }
  },
  components: {
    IconPlus
  }
}

</script>