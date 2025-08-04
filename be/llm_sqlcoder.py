from langchain_ollama import ChatOllama

class SqlCoderLLM:
    def __init__(self, model_name="sqlcoder:7b"):
        self.prompt_file = "prompt.md"
        self.metadata_file = "metadata.sql"
        self.llm = ChatOllama(model=model_name, temperature=0.1)


    def generate_prompt(self, question, prompt_file="prompt_sql.md", metadata_file="metadata.sql"):
        with open(prompt_file, "r") as f:
            prompt = f.read()
        with open(metadata_file, "r") as f:
            table_metadata_string = f.read()
        prompt = prompt.format(
            user_question=question, table_metadata_string=table_metadata_string
        )
        return prompt

    def generate_sql(self, question):
        prompt = self.generate_prompt(question, self.prompt_file, self.metadata_file)
        result = self.llm.invoke(prompt)
        return result

# if __name__ == "__main__":
#     # Parse arguments
#     _default_question="Do we get more sales from customers in New York compared to customers in San Francisco? Give me the total sales for each city, and the difference between the two."
#     parser = argparse.ArgumentParser(description="Run inference on a question")
#     parser.add_argument("-q","--question", type=str, default=_default_question, help="Question to run inference on")
#     args = parser.parse_args()
#     question = args.question
#     print("Loading a model and generating a SQL query for answering your question...")
#     print(run_inference(question))
