
import json
import os
from typing import List, Union
from langchain_core.messages import HumanMessage, SystemMessage

# @todo @davych 未来是需要reasoning的，针对无法进行sql，或者没有参考纬度的询问，则nlu节点就需要额外的human in loop操作
class NLUAgent:
    def __init__(self, llm):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.prompt_file = os.path.join(base_dir, "nlu_prompt.md")
        self.metadata_file = os.path.join(os.path.dirname(base_dir), "db", "metadata.sql")
        self.llm = llm
        self.context = {}

    def generate_prompt(self):
        with open(self.prompt_file, "r") as f:
            prompt = f.read()
        with open(self.metadata_file, "r") as f:
            table_metadata_string = f.read()
        prompt = prompt.format(table_metadata_string=table_metadata_string)
        return prompt
    
    def __call__(self, state):
        user_query = state.get("user_query", [])
        # 类型检查，必须为List[BaseMessage]
        from langchain_core.messages import BaseMessage
        if not (isinstance(user_query, list) and all(isinstance(m, BaseMessage) for m in user_query)):
            raise ValueError("user_query must be a list of BaseMessage, got: {}".format(user_query))
        systemMsg = [SystemMessage(content=self.generate_prompt())]
        history_strs = []
        for idx, msg in enumerate(user_query):
            if idx < len(user_query) - 1:
                history_strs.append(f"[历史消息{idx+1}] {msg.content}")
            else:
                history_strs.append(f"[当前消息] {msg.content}")

        all_history = "\n".join(history_strs)
        humanMsg = [HumanMessage(content=all_history)]
        messages = systemMsg + humanMsg
        response = self.llm.invoke(messages)
        content = response.content if hasattr(response, 'content') else response
        try:
            nlu_result = json.loads(content)
        except json.JSONDecodeError:
            # Fallback to old format if JSON parsing fails
            nlu_result = {
                "translation": content,
                "complete": True,
                "missing_info": None,
                "follow_up_question": None,
                "related_tables": []
            }
        # Update state with parsed result
        state['nlu_result'] = nlu_result
        state['needs_clarification'] = not nlu_result['complete']
        if nlu_result['follow_up_question']:
            state['follow_up_question'] = nlu_result['follow_up_question']
        return state
