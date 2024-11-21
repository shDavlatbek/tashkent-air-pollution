<template>
  <PreloadDiv :class="[isLoaded ? 'fade-out' : '']" />
  <div class="page">
    <HeaderMain :name="name" />
  </div>
</template>

<script>
import { getMe } from "../api/auth";
import HeaderMain from "@/components/HeaderComponent.vue";
import PreloadDiv from "@/components/PreloadDiv.vue";

export default {
  data() {
    return {
      name: null,
      isLoaded: false
    };
  },
  mounted() {
    this.isLoaded = true;
  },
  async beforeCreate() {
    try {
      const response = await getMe();
      this.name = response.full_name;
      console.log(response);
    } catch (error) {
      error.response && error.response.status === 401
          ? this.$router.push("/login")
          : "";
    }
  },
  components: {
    HeaderMain, PreloadDiv
  },
};
</script>
