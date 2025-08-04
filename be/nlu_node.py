
"""
NLU 节点实现：基于 langgraph.agents.create_react_agent 创建 ReAct agent。
"""
import json
from typing import Dict, Any
from nlu_prompt import system_prompt


from langchain_core.messages import HumanMessage, SystemMessage

class NLUAgent:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, state):
        user_query = state.get("user_query", "")
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_query)
        ]
        response = self.llm.invoke(messages)
        content = response.content if hasattr(response, 'content') else response
        parsed_content =  json.loads(content) if isinstance(content, str) else content
        state['nlu_result'] = parsed_content
        return state
