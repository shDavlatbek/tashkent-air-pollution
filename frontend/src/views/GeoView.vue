<template>
  <HeaderText :title="title" :modal-id="modalId" :on-modal-open="loadForm" />
  <teleport to="body">
    <ModalForm :modal-id="modalId" :modal-title="title" :modal-form-confirm="formHandler">
      <template #modal-body>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-6 col-md-12">
              <SelectField label="Qaysi davlat tashkilotiga mansubligi" v-model="addWellForm.organization">
                <option v-for="one in organizations" :key="one.id" :value="one.id">{{ one.name }}</option>
              </SelectField>
            </div>
            <div class="col-lg-6 col-md-12">
              <InputField 
                label="Kuzatuv qudug'i raqami" 
                :required="true" 
                v-model.number="addWellForm.number" 
                type="number" 
              />
            </div>
            <div class="col-lg-6 col-md-12">
              <SelectField 
                label="Kuzatuv burg'u qudug'ining turi" 
                v-model="addWellForm.well_type"
              >
                <option v-for="one in wellTypes" :key="one.id" :value="one.id">{{ one.name }}</option>
              </SelectField>
            </div>
            <div class="col-lg-6 col-md-12">
              <SelectField label="Qaysi stansiya" v-model="addWellForm.station">
                <option v-for="one in stations" :key="one.id" :value="one.id">{{ one.name }}</option>
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
                  <InputField label="Mo'ljal" v-model="addWellForm.address" />
                </div>
                <div class="col-12">
                  <SelectField label="Joylashuv o'rni" v-model="addWellForm.location">
                    <option v-for="one in locations" :key="one.id" :value="one.id">{{ one.name }}</option>
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
                  <InputField class="input-group" type="number" v-model="addWellForm.coordinates.latitude.degree"> 
                    <template #after>
                      <span class="input-group-text">°</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number" v-model="addWellForm.coordinates.latitude.minute"> 
                    <template #after>
                      <span class="input-group-text">'</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number" v-model="addWellForm.coordinates.latitude.second"> 
                    <template #after>
                      <span class="input-group-text">"</span>
                    </template>
                  </InputField>
                </div>
              </div>
              <label class="form-label">Sharqiy uzunlik</label>
              <div class="row">
                <div class="col-4">
                  <InputField class="input-group" type="number" v-model="addWellForm.coordinates.longitude.degree"> 
                    <template #after>
                      <span class="input-group-text">°</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number" v-model="addWellForm.coordinates.longitude.minute"> 
                    <template #after>
                      <span class="input-group-text">'</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number" v-model="addWellForm.coordinates.longitude.second">
                    <template #after>
                      <span class="input-group-text">"</span>
                    </template>
                  </InputField>
                </div>
              </div>
              <label class="form-label">[x; y]</label>
              <div class="row">
                <div class="col-4">
                  <InputField class="input-group" type="number" v-model="addWellForm.coordinates.x"> 
                    <template #after>
                      <span class="input-group-text">x</span>
                    </template>
                  </InputField>
                </div>
                <div class="col-4">
                  <InputField class="input-group" type="number" v-model="addWellForm.coordinates.y"> 
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

  <teleport to="body">
    <ModalDanger 
      :title="modalTitle" 
      :description="modalDesc"
      ref="dangerModal"
    >
      <template #buttons>
        <div class="col">
          <button class="btn w-100" data-bs-dismiss="modal">
            Tushinarli
          </button>
        </div>
      </template>
    </ModalDanger>
  </teleport>
</template>

<script>
import HeaderText from '@/components/HeaderTextComponent.vue';
import ModalForm from '@/components/ModalFormComponent.vue';
import InputField from '@/components/InputField.vue';
import SelectField from '@/components/SelectField.vue';
import ModalDanger from '@/components/ModalDanger.vue';
import { getDistricts, getRegions } from '@/api/common';
import { ref } from 'vue';

export default {
  data() {
    return {
      title: "Gidrogeologik ma'lumotlar",
      modalId: "hydrogeologic-modal",
      addWellForm: {
        number: null,
        region: null,
        district: null,
        address: null,
        well_type: null,
        organization: null,
        location: null,
        station: null,
        coordinates: {
          latitude: {
            degree: null,
            minute: null,
            second: null,
          },
          longitude: {
            degree: null,
            minute: null,
            second: null,
          },
          x: null,
          y: null,
        }
      },
      formLoaded: false,
      wellTypes: {},
      organizations: {},
      locations: {},
      stations: {},
      regions: {},
      districts: {},
      errorMes: false,
      modalDesc: '',
      modalTitle: ''
    }
  },
  computed: {
    formHandler() {
      return () => {
        console.log("Form submitted");
        console.log(this.addWellForm);
      }
    },
    
  },
  setup() {
    const dangerModal = ref();
    return {
      dangerModal
    }
  },
  methods: {
    async changeDistricts(event) {
      try {
        this.districts = await getDistricts(event.target.value);
      } catch (error) {
        this.dangerModal.openModal();
        this.modalTitle = "Tumanlarni yuklashda xatolik yuzaga keldi";
        this.modalDesc = `Xato xabari: ${error.message}`;
        this.errorMes = true;
      }
    },
    async loadForm() {
      if (this.formLoaded) {
        return;
      } else {
        try {
          this.regions = await getRegions();
          // const response = await getNewWellForm();
          // this.wellTypes = response.well_types;
        } catch (error) {
          console.log(error);
          this.modalTitle = "Ma'lumotlarni yuklashda xatolik yuzaga keldi";
          this.dangerModal.openModal();
          this.modalDesc = `Xato xabari: ${error.message}<br>Url: ${error.config.url}`;
          this.errorMes = true;
        }
        
      }
    }
  },
  components: {
    HeaderText, ModalForm, InputField, SelectField, ModalDanger
  },
  async mounted() {
    
  },
}

</script>