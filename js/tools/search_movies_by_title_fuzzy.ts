import { DynamicTool } from "@langchain/core/tools";
import { searchMoviesByTitleFuzzy } from "../db/model/movies";
import yaml from "js-yaml";
import fs from "fs";
import path from "path";

const configPath = path.resolve(__dirname, "./search_movies_by_title_fuzzy.yaml");
const fileContents = fs.readFileSync(configPath, "utf8");
const config = yaml.load(fileContents);

const searchMoviesByTitleFuzzyTool = new DynamicTool({
  ...config,
  func: async (input) => {
    try {
      const results = await searchMoviesByTitleFuzzy(input);
      return JSON.stringify(results);
    } catch (error) {
      return `${error.message}`;
    }
  },
});
export default searchMoviesByTitleFuzzyTool;
