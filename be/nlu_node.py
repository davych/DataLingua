
"""
NLU 节点实现：基于 langgraph.agents.create_react_agent 创建 ReAct agent。
"""
from typing import Dict, Any

from langgraph.prebuilt import create_react_agent

def build_nlu_react_agent(llm, tools=None):
    """
    创建一个基于 LLM 的 ReAct NLU agent。
    llm: 支持 function/tool calling 的大模型实例
    tools: 可选，外部工具列表（如澄清、实体补全等）
    """
    system_prompt = (
        "你是一个专业的数据库自然语言接口。你的任务是分析用户的查询请求，并从中提取意图和关键实体。\n"
        "可识别的意图包括: query_data。\n"
        "你需要提取以下实体: metrics, dimensions, time_range, filters。\n"
        "如果缺少执行查询所必需的实体，请在 missing_entities 字段中注明，并生成 clarification_question。\n"
        "请以JSON格式返回结果。"
    )
    return create_react_agent(
        model=llm,
        tools=tools or [],
        system_prompt=system_prompt
    )
