<template>
  <div>
    <h1>Welcome Back!</h1>
    <p>You're logged in. {{ name }}</p>
  </div>
</template>

<script>
import { getMe } from "../api/auth";

export default {
  data() {
    return {
      name: localStorage.getItem("full_name"),
    };
  },
  async created() {
    try {
      const response = await getMe();
      console.log(response);
    } catch (error) {
      this.$router.push("/login");
    }
  },
};
</script>
