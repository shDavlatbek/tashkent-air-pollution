import { reqApi } from "./base";

export const getNewWellForm = async () => {
  return (await reqApi("/well/add")).data;
};