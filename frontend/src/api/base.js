import { api } from ".";

export const reqApi = async (route, params = {}, method = 'GET') => {
  try {
    const config = {
      method,
      url: route,
      headers: { 'Content-Type': 'application/json' },
    };

    if (method === 'GET' || method === 'DELETE') {
      config.params = params;
    } else {
      config.data = params;
    }

    const response = await api.request(config);
    return response;
  } catch (error) {
    console.error('API error:', error.message || error);
    throw error;
  }
};