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
      verbose: true, // 显示详细执行过程
      maxIterations: 5, // 允许多轮推理
      handleParsingErrors: true, // 处理解析错误
      returnIntermediateSteps: true, // 返回中间步骤
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
      input: "how many movies belong to the 'Action' genre, could you please help me find out them?",
    });

    console.log(`\n🎯 结果：${result.output}\n`);
    if (result.intermediateSteps && result.intermediateSteps.length > 0) {
      console.log("🔍 推理过程：");
      result.intermediateSteps.forEach((step, index) => {
        console.log(`步骤 ${index + 1}:`);
        console.log(`  Action: ${step.action.tool}`);
        console.log(`  Input: ${step.action.toolInput}`);
        console.log(`  Output: ${step.observation}`);
      });
    }
  } catch (error) {
    console.error("❌ 启动助手失败：", error);
  }
})().catch((error) => {
  console.error("❌ 启动失败：", error);
});
