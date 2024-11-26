import { reqApi } from "./base";

export const getRegions = async () => {
  return (await reqApi("/regions")).data;
};

export const getDistricts = async (region_id=null) => {
  if (!region_id) {
    return (await reqApi("/districts")).data;
  }
  return (await reqApi("/districts", {region_id: region_id})).data;
};