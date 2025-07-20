import { ChatOllama } from "@langchain/ollama";

(async () => {
  const model = new ChatOllama({
    model: "codellama:13b", // Default value.
  });

  const result = await model.invoke(["human", "Hello, how are you?"]);
  console.log(result);
})().catch((error) => {
  console.error("Error:", error);
});
