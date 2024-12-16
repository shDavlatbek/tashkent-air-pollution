import { reqApi } from "./base";

const PREFIX = "/station";

export const addStation = async (data) => {
  return (await reqApi(`${PREFIX}/add`, data, "POST")).data;
};

export const getStations = async () => {
  return (await reqApi(PREFIX)).data;
};

export const getWell = async (id) => {
  return (await reqApi(`/geo/${id}`)).data;
};

export const getParameterNames = async () => {
  return (await reqApi(`/parameter-names`)).data;
};

export const getParameter = async (well_id) => {
  return (await reqApi(`/geo/parameter`, {well: well_id})).data;
};