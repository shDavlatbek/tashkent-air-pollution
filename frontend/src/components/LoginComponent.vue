<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="email">Email:</label>
        <input id="email" v-model="email" type="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import { login } from "../api/auth";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async handleLogin() {
      let res;
      try {
        res = await login(this.email, this.password);
        alert(`Succesfully loged. ${JSON.stringify(res)}`);
        localStorage.setItem("full_name", res.full_name);
        this.$router.push("/authenticated");
      } catch (error) {
        alert(`Login failed. Please check your credentials. ${JSON.stringify(res)}`);
      }
    },
  },
};
</script>

<style scoped>
form {
  max-width: 400px;
  margin: 0 auto;
}
</style>
