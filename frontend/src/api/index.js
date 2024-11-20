import axios from "axios";

export const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL, // FastAPI backend URL
  withCredentials: true, // Ensures cookies are sent with requests
});