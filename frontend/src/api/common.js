import { reqApi } from "./base";

export const getRegions = async () => {
  return response = await reqApi.get("/regions");;
};

export const getDistricts = async (region_id) => {
  return await reqApi.get("/districts", {region_id: region_id});
};