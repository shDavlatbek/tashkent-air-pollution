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
import { getStationsParams } from "@/api/station";

export default {
  data() {
    return {
      dashboard: null,
      stations: []
    };
  },
  
  methods: {
    loadFrame(event){
      const iframe = event.target;
      try {
        const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
        iframe.style.height = iframeDocument.body.scrollHeight + 'px';
      } catch (error) {
        console.error("Unable to adjust iframe height:", error);
      }
    },
    utcRoundedTime() {
      const now = new Date();
      return new Date(Date.UTC(
        now.getUTCFullYear(),
        now.getUTCMonth(),
        now.getUTCDate(),
        now.getUTCHours(), // Keep hours
        0,                 // Set minutes to 0
        0,                 // Set seconds to 0
        0                  // Set milliseconds to 0
      ));
    },
    utcTime10daysAgo() {
      const now = new Date();
      return new Date(Date.UTC(
        now.getUTCFullYear(),
        now.getUTCMonth(),
        now.getUTCDate() - 10,
        now.getUTCHours(), // Keep hours
        0,                 // Set minutes to 0
        0,                 // Set seconds to 0
        0                  // Set milliseconds to 0
      ));
    }
  },

  async mounted() {
    this.stations = await getStationsParams(
      this.utcTime10daysAgo(),
      this.utcRoundedTime(),
    );
  },

  components: { AQIMap }
};
</script>
