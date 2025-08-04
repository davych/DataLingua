
import json
import os
from langchain_core.messages import HumanMessage, SystemMessage

class NLUAgent:
    def __init__(self, llm):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.prompt_file = os.path.join(base_dir, "nlu_prompt.md")
        self.metadata_file = os.path.join(os.path.dirname(base_dir), "db", "metadata.sql")
        self.llm = llm

    def generate_prompt(self):
        with open(self.prompt_file, "r") as f:
            prompt = f.read()
        with open(self.metadata_file, "r") as f:
            table_metadata_string = f.read()
        prompt = prompt.format(table_metadata_string=table_metadata_string)
        return prompt
    
    def __call__(self, state):
        user_query = state.get("user_query", "")
        messages = [
            SystemMessage(content=self.generate_prompt()),
            HumanMessage(content=user_query)
        ]
        response = self.llm.invoke(messages)
        content = response.content if hasattr(response, 'content') else response
        parsed_content =  json.loads(content) if isinstance(content, str) else content
        state['nlu_result'] = parsed_content
        return state
