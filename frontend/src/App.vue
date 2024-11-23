<template>
  <component :is="currentLayout">
  </component>
</template>

<script>
import { getMe } from './api/auth';
import MainLayout from './layout/MainLayout.vue';
import PreloadDiv from './components/PreloadDiv.vue';
import EmptyLayout from './layout/EmptyLayout.vue';

const layout = {
  main: MainLayout,
  empty: EmptyLayout,
};

export default {
  name: 'App',
  data() {
    return {
      currentLayout: PreloadDiv, // Default to PreloadDiv while loading
    };
  },
  async created() {
    // Handle auth-based layout assignment
    await this.setLayout();
  },
  watch: {
    // Watch for route changes and update layout dynamically
    $route: {
      immediate: true,
      handler() {
        this.setLayout();
      },
    },
  },
  methods: {
    async setLayout() {
      // Handle authentication and layout assignment
      if (this.$route.meta.auth) {
        try {
          const response = await getMe();
          console.log(response); // Log the user data (optional)
        } catch (error) {
          if (error.response && error.response.status === 401) {
            return this.$router.push('/login');
          }
        }
      }

      this.currentLayout = layout[this.$route.meta.layout] || EmptyLayout;
    },
  },
  components: {
    MainLayout,
    PreloadDiv,
    EmptyLayout,
  },
};
</script>

<style>
#app{
  position: relative;
  z-index: 1;
}
</style>
