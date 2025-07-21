import { ChatOllama } from "@langchain/ollama";
import { createReactAgent } from "langchain/agents";
import { AgentExecutor } from "langchain/agents";
import {
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  SystemMessagePromptTemplate,
} from "@langchain/core/prompts";
import { systemPrompt, humanPrompt } from "./template";
import getAllMoviesTool from "./tools/get_all_movies";
import searchMoviesByTitleFuzzyTool from "./tools/search_movies_by_title_fuzzy";
import searchMoviesBelongGenreTool from "./tools/search_movies_belong_genre";

const llm = new ChatOllama({
  model: "deepseek-r1:32b",
  baseUrl: "http://localhost:11434",
  temperature: 0.5,
});

async function createMathGeniusAgent() {
  try {
    const customPrompt = ChatPromptTemplate.fromMessages([
      SystemMessagePromptTemplate.fromTemplate(systemPrompt),
      HumanMessagePromptTemplate.fromTemplate(humanPrompt),
    ]);

    const tools = [
        searchMoviesByTitleFuzzyTool, getAllMoviesTool, searchMoviesBelongGenreTool
    ];

    const agent = await createReactAgent({
      llm,
      tools,
      prompt: customPrompt,
    });

    const agentExecutor = new AgentExecutor({
      agent,
      tools,
      verbose: true,
      maxIterations: 5,
      handleParsingErrors: true,
      returnIntermediateSteps: true, 
    });

    return agentExecutor;
  } catch (error) {
    console.error("创建 Agent 失败：", error);
    throw error;
  }
}

(async () => {
  try {
    const agent = await createMathGeniusAgent();
    const result = await agent.invoke({
      input: "Help me get all movies?",
    });

    console.log(`\n🎯 Result: ${result.output}\n`);
  } catch (error) {
    console.error("❌ Fail", error);
  }
})().catch((error) => {
  console.error("❌ Fail", error);
});
