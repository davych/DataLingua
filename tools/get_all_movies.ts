import { DynamicTool } from "@langchain/core/tools";
import { getAllMovies } from "../db/model/movies";
import yaml from "js-yaml";
import fs from "fs";
import path from "path";

const configPath = path.resolve(__dirname, "./get_all_movies.yaml");
const fileContents = fs.readFileSync(configPath, "utf8");
const config = yaml.load(fileContents);

const getAllMoviesTool = new DynamicTool({
  ...config,
  func: async () => {
    try {
      const results = await getAllMovies();
      return JSON.stringify(results);
    } catch (error) {
      return `${error.message}`;
    }
  },
});
export default getAllMoviesTool;
