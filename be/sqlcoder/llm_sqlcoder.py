
import os
from langchain_ollama import ChatOllama

class SqlCoderLLM:
    import os
    def __init__(self, model_name="sqlcoder:7b"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.prompt_file = os.path.join(base_dir, "prompt_sql.md")
        self.metadata_file = os.path.join(os.path.dirname(base_dir), "db", "metadata.sql")
        self.llm = ChatOllama(model=model_name, temperature=0.1)


    def generate_prompt(self, question):
        with open(self.prompt_file, "r") as f:
            prompt = f.read()
        with open(self.metadata_file, "r") as f:
            table_metadata_string = f.read()
        prompt = prompt.format(
            user_question=question, table_metadata_string=table_metadata_string
        )
        return prompt

    def generate_sql(self, question):
        prompt = self.generate_prompt(question)
        result = self.llm.invoke(prompt)
        # content='<s> SELECT COUNT(DISTINCT artist.artistid) AS number_of_artists FROM artist;'
        sql_content = result.content if hasattr(result, 'content') else ''
        if isinstance(sql_content, list):
            sql_str = " ".join(str(item) for item in sql_content)
        else:
            sql_str = str(sql_content)
        sql_str = sql_str.replace('<s>', '').strip()
        sql_str = sql_str.replace(';', '').strip()
        print(f"Final SQL: {sql_str}")  # Final output for debugging
        return sql_str