import { reqApi } from "./base";

export const getNewWellForm = async () => {
  return (await reqApi("/geo/add")).data;
};

export const addNewWell = async (data) => {
  return (await reqApi("/geo/add", data, "POST")).data;
};

export const getWells = async () => {
  return (await reqApi("/geo/")).data;
};