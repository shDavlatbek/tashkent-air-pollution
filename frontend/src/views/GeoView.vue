<template>
  <HeaderText :title="title" :modal-id="modalId" />
  <teleport to="body">
    <ModalForm :modal-id="modalId" :modal-title="title" :modal-form-confirm="formHandler">
      <template v-slot:modal-body>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-6 col-md-12">
              <div class="mb-3">
                <label class="form-label required">Qaysi davlat tashkilotiga mansubligi</label>
                <select class="form-select">
                  <option value="1">Private</option>
                  <option value="2">Public</option>
                  <option value="3">Hidden</option>
                </select>
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="mb-3">
                <label class="form-label required">Kuzatuv qudug'i raqami</label>
                <input type="number" class="form-control" name="example-text-input" placeholder="Your report name">
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="mb-3">
                <label class="form-label required">Kuzatuv burg'u qudug'ining turi</label>
                <select class="form-select">
                  <option value="1">Private</option>
                  <option value="2">Public</option>
                  <option value="3">Hidden</option>
                </select>
              </div>
            </div>
            <div class="col-lg-6 col-md-12">
              <div class="mb-3">
                <label class="form-label required">Qaysi stansiya</label>
                <select class="form-select">
                  <option value="1">Private</option>
                  <option value="2">Public</option>
                  <option value="3">Hidden</option>
                </select>
              </div>
            </div>
          </div>
        </div>

        <div class="modal-body">
          <div class="row">
            <div class="col-lg-6">
              <div class="row">
                <div class="col-12">
                  <div class="mb-3">
                    <label class="form-label required">Viloyat nomi</label>
                    <RegionSelect :regions="regions" @change="changeDistricts" v-model="addWellForm.region" class="form-select" />
                  </div>
                </div>
                <div class="col-12">
                  <div class="mb-3">
                    <label class="form-label required">Tuman nomi</label>
                    <DistrictSelect :districts="districts" v-model="addWellForm.district" class="form-select" />
                  </div>
                </div>
                <div class="col-12">
                  <div class="mb-3">
                    <label class="form-label required">Mo'ljal</label>
                    <input type="text" class="form-control">
                  </div>
                </div>
                <div class="col-12">
                  <div class="mb-3">
                    <label class="form-label required">Joylashuv o'rni</label>
                    <select class="form-select">
                      <option value="1">Private</option>
                      <option value="2">Public</option>
                      <option value="3">Hidden</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="mb-3">
                <label class="form-label">*</label>
                <div class="form-control-plaintext">Kuzatuv burg'u qudug'ining koordinatasi</div>
              </div>
              <label class="form-label">Shimoliy kenglik</label>
              <div class="row">
                <div class="col-4">
                  <div class="input-group mb-3">
                    <input type="number" class="form-control" autocomplete="off">
                    <span class="input-group-text">°</span>
                  </div>
                </div>
                <div class="col-4">
                  <div class="input-group mb-3">
                    <input type="number" class="form-control" autocomplete="off">
                    <span class="input-group-text">'</span>
                  </div>
                </div>
                <div class="col-4">
                  <div class="input-group mb-3">
                    <input type="number" class="form-control" autocomplete="off">
                    <span class="input-group-text">"</span>
                  </div>
                </div>
              </div>
              <label class="form-label">Sharqiy uzunlik</label>
              <div class="row">
                <div class="col-4">
                  <div class="input-group mb-3">
                    <input type="number" class="form-control" autocomplete="off">
                    <span class="input-group-text">°</span>
                  </div>
                </div>
                <div class="col-4">
                  <div class="input-group mb-3">
                    <input type="number" class="form-control" autocomplete="off">
                    <span class="input-group-text">'</span>
                  </div>
                </div>
                <div class="col-4">
                  <div class="input-group mb-3">
                    <input type="number" class="form-control" autocomplete="off">
                    <span class="input-group-text">"</span>
                  </div>
                </div>
              </div>
              <label class="form-label">[x; y]</label>
              <div class="row">
                <div class="col-4">
                  <div class="input-group mb-3">
                    <input type="number" class="form-control" autocomplete="off">
                    <span class="input-group-text">x</span>
                  </div>
                </div>
                <div class="col-4">
                  <div class="input-group mb-3">
                    <input type="number" class="form-control" autocomplete="off">
                    <span class="input-group-text">y</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
    </ModalForm>
  </teleport>
</template>

<script>
import HeaderText from '@/components/HeaderTextComponent.vue';
import ModalForm from '@/components/ModalFormComponent.vue';
import RegionSelect from '@/components/RegionSelect.vue';
import DistrictSelect from '@/components/DistrictSelect.vue';
import { getDistricts, getRegions } from '@/api/common';

export default {
  data() {
    return {
      title: "Gidrogeologik ma'lumotlar",
      modalId: "hydrogeologic-modal",
      addWellForm: {
        name: '',
        region: '',
        district: '',
        address: '',
      },
      regions: [],
      districts: [],
    }
  },
  computed: {
    formHandler() {
      return () => {
        console.log("Form submitted");
      }
    },
  },
  methods: {
    async changeDistricts(event) {
      this.districts = await getDistricts(event.target.value);
    },
  },
  components: {
    HeaderText, ModalForm, RegionSelect, DistrictSelect,
  },
  async mounted() {
    this.regions = await getRegions();
  },
}

</script>