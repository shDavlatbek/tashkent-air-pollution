<template>
  <div>
    <h1>Welcome to the FastAPI + Vue.js App</h1>
    <router-link to="/login">Login</router-link> | 
    <router-link to="/register">Sign Up</router-link>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 2rem;
}
</style>
