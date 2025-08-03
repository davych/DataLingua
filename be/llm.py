from langchain_community.llms import Ollama

# Connect to local Ollama instance (default: http://localhost:11434)
llm = Ollama(
    model="llama3.1:latest",  # or any model you have pulled locally, e.g., "mistral", "phi"
)

# Example usage: generate a completion
response = llm.invoke("What is the capital of France?")
print(response)