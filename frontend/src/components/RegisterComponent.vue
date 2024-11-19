<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="handleRegister">
      <div>
        <label for="full_name">Full Name:</label>
        <input id="full_name" v-model="full_name" type="text" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input id="email" v-model="email" type="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import { register } from "../api/auth";

export default {
  data() {
    return {
      full_name: "",
      email: "",
      password: "",
    };
  },
  methods: {
    async handleRegister() {
      let res;
      try {
        res = await register(this.full_name, this.email, this.password);
        alert(`Registration successful! ${JSON.stringify(res)}`);
        this.$router.push("/login");
      } catch (error) {
        alert(`Registration failed. Try again. ${JSON.stringify(res) || "No response"}`);
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
