<template>
  <div class="page-body">
    <div class="container-xl">
      <iframe id="myIframe" @load="loadFrame" :src="dashboard" style="width: 100%; border: none; height: 85vh"></iframe>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dashboard: null,
      api: axios.create({ baseURL: 'https://opendata-back.tashkent.uz/oz/api/data/all/133/?format=json' })
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
};
</script>
