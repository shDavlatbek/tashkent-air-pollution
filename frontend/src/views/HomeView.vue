<template>
  <div class="page-body">
    <div class="container-xl">
      <div class="row">
        <div class="col-4">
      
        </div>
        <div class="col-8">
          <div class="card mb-4">
            <div class="card-header">
              <h3 class="card-title">Havo sifati interpolyatsiyasi</h3>
            </div>
            <div class="card-body">
              <div class="badges-list">
                <span class="badge text-white" style="background-color: #00e400;">Yaxshi</span>
                <span class="badge text-white" style="background-color: #f7D543;">O‘rtacha</span>
                <span class="badge text-white" style="background-color: #ff7e00;">Nozik guruhlar uchun zararli</span>
                <span class="badge text-white" style="background-color: #E95F5E;">Zararli</span>
                <span class="badge text-white" style="background-color: #9168A1;">Juda zararli</span>
              </div>
            </div>
            <AQIMap :stations="stations" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AQIMap from "@/components/AQIMap.vue";
import axios from "axios";

export default {
  data() {
    return {
      dashboard: null,
      api: axios.create({ baseURL: 'https://opendata-back.tashkent.uz/oz/api/data/all/133/?format=json' }),
      stations: [
        { id: 1, name: "Station 1", lat: 41.2995, lng: 69.2401, aqi: 50 },
        { id: 2, name: "Station 2", lat: 41.3089, lng: 69.2800, aqi: 132 },
        { id: 3, name: "Station 3", lat: 41.2899, lng: 69.2654, aqi: 142 },
      ]
    };
  },
  
  methods: {
    async getDashboard() {
      return await this.api.get().then((res) => {
        return res.data.iframe_link_oz;
      });
    },
    loadFrame(event){
      const iframe = event.target;
      try {
        const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
        iframe.style.height = iframeDocument.body.scrollHeight + 'px';
      } catch (error) {
        console.error("Unable to adjust iframe height:", error);
      }
    }
  },

  async mounted() {
    this.dashboard = await this.getDashboard();
  },

  components: { AQIMap }
};
</script>
