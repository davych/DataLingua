
"""
NLU 节点实现：基于 langgraph.agents.create_react_agent 创建 ReAct agent。
"""
import json
from typing import Dict, Any
from nlu_prompt import system_prompt


from langchain_core.messages import HumanMessage, SystemMessage

class NLUAgent:
    """
    官方推荐结构：声明 NLU agent 类，兼容 langgraph StateGraph。
    """
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, state):
        # 将 state 映射为消息列表
        user_query = state.get("user_query", "")
        # 调用 LLM
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_query)
        ]
        response = self.llm.invoke(messages)
        content = response.content if hasattr(response, 'content') else response
        # json dump
        parsed_content =  json.loads(content) if isinstance(content, str) else content
        print("LLM 返回:", parsed_content)
        state['nlu_result'] = parsed_content
        # 你可以在这里做更复杂的解析/结构化
        return state

def build_nlu_react_agent(llm, tools=None):
    """
    返回自定义 NLUAgent 实例，兼容 langgraph。
    """
    return NLUAgent(llm)
