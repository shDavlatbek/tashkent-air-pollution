<template>
  <div class="page-body" v-if="well">
    <div class="container-xl">
      <div class="card mb-4">
        <div class="card-header">
          <h3 class="card-title">Quduq ma'lumotlari</h3>
          <div class="card-actions">
            <a href="#" data-bs-toggle="modal" data-bs-target="">
              Tahrirlash
              <IconPencil class="icon" stroke="2" />
            </a>
          </div>
        </div>
        <div class="card-body">
          <div class="datagrid">
            <div class="datagrid-item">
              <div class="datagrid-title">Quduq raqami</div>
              <div class="datagrid-content">{{ well?.number ? well?.number : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Stansiya nomi</div>
              <div class="datagrid-content">{{ well?.station ? well?.station?.name : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Viloyat</div>
              <div class="datagrid-content">{{ well?.region ? well?.region?.name : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Tuman</div>
              <div class="datagrid-content">{{ well?.district ? well?.district?.name : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Joylashuv o'rni</div>
              <div class="datagrid-content">{{ well?.location ? well?.location?.name : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Quduq turi</div>
              <div class="datagrid-content">{{ well?.well_type ? well?.well_type?.name : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Mo'ljal</div>
              <div class="datagrid-content">{{ well?.address?.name ? well?.address?.name : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Tashkilot</div>
              <div class="datagrid-content">{{ well?.organization ?  well?.organization?.name : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Shimoliy kenglik</div>
              <div class="datagrid-content">{{ latitude }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Sharqiy kenglik</div>
              <div class="datagrid-content">{{ longitude }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">[X, Y]</div>
              <div class="datagrid-content">{{ well?.coordinate?.x ? well?.coordinate?.x : noInfoMes }}:{{ well?.coordinate?.y ? well?.coordinate?.y : noInfoMes }}</div>
            </div>
            <div class="datagrid-item">
              <div class="datagrid-title">Qo'shilgan vaqti</div>
              <div class="datagrid-content">{{ well?.created_at ? format(new Date(well?.created_at), 'dd.MM.yyyy HH:mm:ss') : noInfoMes }}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="row row-cards">
        <div class="col">
          <div class="card">
            <div class="table-responsive">
              <table class="table table-vcenter card-table table-bordered">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Title</th>
                    <th>Email</th>
                    <th>Role</th>
                    <th class="w-1"></th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td >Paweł Kuna</td>
                    <td class="text-secondary" >
                      UI Designer, Training
                    </td>
                    <td class="text-secondary" ><a href="#" class="text-reset">paweluna@howstuffworks.com</a></td>
                    <td class="text-secondary" >
                      User
                    </td>
                    <td>
                      <a href="#">Edit</a>
                    </td>
                  </tr>
                  <tr>
                    <td >Jeffie Lewzey</td>
                    <td class="text-secondary" >
                      Chemical Engineer, Support
                    </td>
                    <td class="text-secondary" ><a href="#" class="text-reset">jlewzey1@seesaa.net</a></td>
                    <td class="text-secondary" >
                      Admin
                    </td>
                    <td>
                      <a href="#">Edit</a>
                    </td>
                  </tr>
                  <tr>
                    <td >Mallory Hulme</td>
                    <td class="text-secondary" >
                      Geologist IV, Support
                    </td>
                    <td class="text-secondary" ><a href="#" class="text-reset">mhulme2@domainmarket.com</a></td>
                    <td class="text-secondary" >
                      User
                    </td>
                    <td>
                      <a href="#">Edit</a>
                    </td>
                  </tr>
                  <tr>
                    <td >Dunn Slane</td>
                    <td class="text-secondary" >
                      Research Nurse, Sales
                    </td>
                    <td class="text-secondary" ><a href="#" class="text-reset">dslane3@epa.gov</a></td>
                    <td class="text-secondary" >
                      Owner
                    </td>
                    <td>
                      <a href="#">Edit</a>
                    </td>
                  </tr>
                  <tr>
                    <td >Emmy Levet</td>
                    <td class="text-secondary" >
                      VP Product Management, Accounting
                    </td>
                    <td class="text-secondary" ><a href="#" class="text-reset">elevet4@senate.gov</a></td>
                    <td class="text-secondary" >
                      Admin
                    </td>
                    <td>
                      <a href="#">Edit</a>
                    </td>
                  </tr>
                  <tr>
                    <td >Maryjo Lebarree</td>
                    <td class="text-secondary" >
                      Civil Engineer, Product Management
                    </td>
                    <td class="text-secondary" ><a href="#" class="text-reset">mlebarree5@unc.edu</a></td>
                    <td class="text-secondary" >
                      User
                    </td>
                    <td>
                      <a href="#">Edit</a>
                    </td>
                  </tr>
                  <tr>
                    <td >Egan Poetz</td>
                    <td class="text-secondary" >
                      Research Nurse, Engineering
                    </td>
                    <td class="text-secondary" ><a href="#" class="text-reset">epoetz6@free.fr</a></td>
                    <td class="text-secondary" >
                      Admin
                    </td>
                    <td>
                      <a href="#">Edit</a>
                    </td>
                  </tr>
                  <tr>
                    <td >Kellie Skingley</td>
                    <td class="text-secondary" >
                      Teacher, Services
                    </td> 
                    <td class="text-secondary" ><a href="#" class="text-reset">kskingley7@columbia.edu</a></td>
                    <td class="text-secondary" >
                      Owner
                    </td>
                    <td>
                      <a href="#">Edit</a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    
  </div>

  <teleport to="body">
    <ModalAlert :title="modalTitle" :description="modalDesc" ref="modalAlert" :type="modalType">
      <template #buttons>
        <div class="col">
          <button class="btn w-100" @click="modalOnCloseFunc" data-bs-dismiss="modal" data-bs-target="#modal-alert">
            Tushinarli
          </button>
        </div>
      </template>
    </ModalAlert>
  </teleport>
</template>

<script>
import { getWell } from '@/api/geo';
import { ref } from 'vue';
import { format } from 'date-fns';
import { IconPencil } from '@tabler/icons-vue'


export default {
  data: () => ({
    well: null,
    modalTitle: '',
    modalDesc: '',
    modalType: '',
    noInfoMes: '-',
    modalOnCloseFunc: () => { },
  }),

  components: {
    IconPencil
  },

  setup() {
    const modalAlert = ref();
    return {
      modalAlert
    }
  },

  computed: {
    format() {
      return format;
    },
    longitude(){
      const { longitude_degree, longitude_minute, longitude_second } = this.well?.coordinate ?? {};
      return `${longitude_degree ?? ''}°${longitude_minute ?? ''}"${longitude_second ?? ''}'`;
    },
    latitude() {
      const { latitude_degree, latitude_minute, latitude_second } = this.well?.coordinate ?? {};
      return `${latitude_degree ?? ''}°${latitude_minute ?? ''}"${latitude_second ?? ''}'`;
    }
  },

  async mounted() {
    const wellId = this.$route?.params?.id; // Access $route in the mounted hook
    if (wellId) {
      try {
        this.well = await getWell(wellId);
        console.log(this.well);
        
      } catch (error) {
        console.error('Error fetching well data:', error);
        this.modalAlert.openModal();
        this.modalTitle = "Ma'lumotlarni yuklashda xatolik yuzaga keldi";
        this.modalDesc = `Xato xabari: ${error.message}`;
        this.modalType = 'danger';
      }
    } else {
      console.error('No wellId found in route parameters.');
    }
  },
};
</script>
