<template>
  <HeaderText :title="title" :modal-id="modalId" :on-modal-open="loadForm" />
  <teleport to="body">
    <ModalForm :modal-id="modalId" :modal-title="title" :modal-form-confirm="formHandler">
      <template #modal-body>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-6 col-md-12">
              <SelectField label="Qaysi davlat tashkilotiga mansubligi">
                <option value="1">Private</option>
                <option value="2">Public</option>
                <option value="3">Hidden</option>
              </SelectField>
            </div>
            <div class="col-lg-6 col-md-12">
              <InputField label="Kuzatuv qudug'i raqami" :required="true" v-model.number="addWellForm.number" type="number" />
            </div>
            <div class="col-lg-6 col-md-12">
              <SelectField label="Kuzatuv burg'u qudug'ining turi" :required="true" v-model="addWellForm.type">
                <option v-for="type in wellTypes" :key="type.id" :value="type.id">{{ type.name }}</option>
              </SelectField>
            </div>
            <div class="col-lg-6 col-md-12">
              <SelectField label="Qaysi stansiya">
                <option value="1">Private</option>
                <option value="2">Public</option>
                <option value="3">Hidden</option>
              </SelectField>
            </div>
          </div>
        </div>

        <div class="modal-body">
          <div class="row">
            <div class="col-lg-6">
              <div class="row">
                <div class="col-12">
                  <SelectField
                    label="Viloyat nomi"
                    empty-value="0"
                    @change="changeDistricts" 
                    v-model="addWellForm.region" 
                  >
                    <option v-for="region in regions" :key="region.id" :value="region.id">
                      {{ region.name }}
                    </option>
                  </SelectField>
                </div>
                <div class="col-12">
                  <SelectField
                    label="Tuman nomi"
                    empty-value="0"
                    v-model="addWellForm.district" 
                  >
                    <option v-for="district in districts" :key="district.id" :value="district.id">
                      {{ district.name }}
                    </option>
                  </SelectField>
                </div>
                <div class="col-12">
                  <InputField label="Mo'ljal" />
                </div>
                <div class="col-12">
                  <SelectField label="Joylashuv o'rni">
                    <option value="1">Private</option>
                    <option value="2">Public</option>
                    <option value="3">Hidden</option>
                  </SelectField>
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
                  <InputField class="input-group" type="number"> 
                    <template #after>
                      <span class="input-group-text">°</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number"> 
                    <template #after>
                      <span class="input-group-text">'</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number"> 
                    <template #after>
                      <span class="input-group-text">"</span>
                    </template>
                  </InputField>
                </div>
              </div>
              <label class="form-label">Sharqiy uzunlik</label>
              <div class="row">
                <div class="col-4">
                  <InputField class="input-group" type="number"> 
                    <template #after>
                      <span class="input-group-text">°</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number"> 
                    <template #after>
                      <span class="input-group-text">'</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number"> 
                    <template #after>
                      <span class="input-group-text">"</span>
                    </template>
                  </InputField>
                </div>
              </div>
              <label class="form-label">[x; y]</label>
              <div class="row">
                <div class="col-4">
                  <InputField class="input-group" type="number"> 
                    <template #after>
                      <span class="input-group-text">x</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number"> 
                    <template #after>
                      <span class="input-group-text">y</span>
                    </template>
                  </InputField>
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
import InputField from '@/components/InputField.vue';
import SelectField from '@/components/SelectField.vue';
import { getDistricts, getRegions } from '@/api/common';

export default {
  data() {
    return {
      title: "Gidrogeologik ma'lumotlar",
      modalId: "hydrogeologic-modal",
      addWellForm: {
        number: '',
        region: '',
        district: '',
        address: '',
      },
      formLoaded: false,
      wellTypes: {},
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
    loadForm() {
      return async () => {
        if (this.formLoaded) {
          return;
        } else {
          this.regions = await getRegions();
          this.formLoaded = true;
        }
      }
    }
  },
  methods: {
    async changeDistricts(event) {
      this.districts = await getDistricts(event.target.value);
    },
  },
  components: {
    HeaderText, ModalForm, InputField, SelectField
  },
  async mounted() {
    
  },
}

</script>