import { reqApi } from "./base";

export const getRegions = async () => {
  return await reqApi("/regions");
};

export const getDistricts = async (region_id) => {
  return await reqApi("/districts", {region_id: region_id});
};