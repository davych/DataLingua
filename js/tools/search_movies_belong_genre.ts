import { DynamicTool } from "@langchain/core/tools";
import { searchMoviesByGenreName } from "../db/model/movies";
import yaml from "js-yaml";
import fs from "fs";
import path from "path";

const configPath = path.resolve(__dirname, "./search_movies_belong_genre.yaml");
const fileContents = fs.readFileSync(configPath, "utf8");
const config = yaml.load(fileContents);

const searchMoviesBelongGenreTool = new DynamicTool({
  ...config,
  func: async (input) => {
    try {
      console.log(`🔧 工具调用 searchMoviesBelongGenreTool --- - 输入: ${input}`);
      const results = await searchMoviesByGenreName(input);
      console.log(`🔧 工具调用 searchMoviesBelongGenreTool --- - 输出: ${JSON.stringify(results)}`);
      return JSON.stringify(results);
    } catch (error) {
      return `${error.message}`;
    }
  },
});
export default searchMoviesBelongGenreTool;
