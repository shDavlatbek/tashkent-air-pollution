import { api } from ".";

export const login = async (email, password) => {
  const data = new URLSearchParams();
  data.append("username", email);
  data.append("password", password);

  const response = await api.post("/auth/login", data, {
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  });
  return response.data;
};

export const logout = async () => {
  const response = await api.post("/auth/logout");
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

export const getMe = async () => {
  const response = await api.get("/users/me");
  return response.data;
};