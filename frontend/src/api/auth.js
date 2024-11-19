import axios from "axios";

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL, // FastAPI backend URL
  withCredentials: true, // Ensures cookies are sent with requests
});

export const login = async (email, password) => {
  const data = new URLSearchParams();
  data.append("username", email);
  data.append("password", password);

  const response = await api.post("/auth/login", data, {
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  });
  return response.data;
};

export const register = async (full_name, email, password) => {
  const response = await api.post("/auth/register", 
    { full_name, email, password }, 
    {headers: { "Content-Type": "application/json" }}
  );
  return response.data;
};

export const getProtectedRoute = async () => {
  const response = await api.get("/protected-route");
  return response.data;
};
