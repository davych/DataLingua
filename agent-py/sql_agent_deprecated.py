from langchain_ollama import ChatOllama
from db.connection import db
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List, Dict, Any
import operator
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage, AIMessage
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
_ = load_dotenv()

llm = ChatOllama(model="MFDoom/deepseek-r1-tool-calling:14b")


class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]

class Agent:
    def __init__(self, model, tools: List, system: str = ""):
        self.system = system
        self.tools: Dict[str, Any] = {t.name: t for t in tools}
        self.model = model.bind_tools(tools)
        
        # 构建图
        graph = StateGraph(AgentState)
        graph.add_node("llm", self.call_ollama)
        graph.add_node("action", self.take_action)
        
        graph.add_conditional_edges(
            "llm",
            self.exists_action,
            {True: "action", False: END}
        )
        graph.add_edge("action", "llm")
        graph.set_entry_point("llm")
        
        self.graph = graph.compile()

    def exists_action(self, state: AgentState) -> bool:
        """检查最后一条消息是否包含工具调用"""
        last_message = state['messages'][-1]
        
        # 类型安全检查：只有 AIMessage 才可能有 tool_calls
        if isinstance(last_message, AIMessage):
            return bool(getattr(last_message, 'tool_calls', None))
        
        return False

    def call_ollama(self, state: AgentState) -> Dict[str, List[AnyMessage]]:
        """调用 LLM"""
        messages = state['messages'].copy()
        
        # 添加系统消息（如果有的话）
        if self.system:
            # 检查是否已经有系统消息
            if not messages or not isinstance(messages[0], SystemMessage):
                messages = [SystemMessage(content=self.system)] + messages
        
        try:
            message = self.model.invoke(messages)
            return {'messages': [message]}
        except Exception as e:
            print(f"LLM 调用错误: {e}")
            error_message = AIMessage(content=f"抱歉，处理请求时出现错误: {str(e)}")
            return {'messages': [error_message]}

    def take_action(self, state: AgentState) -> Dict[str, List[ToolMessage]]:
        """执行工具调用"""
        last_message = state['messages'][-1]
        
        # 安全检查
        if not isinstance(last_message, AIMessage):
            print("错误：最后一条消息不是 AIMessage")
            return {'messages': []}
        
        tool_calls = getattr(last_message, 'tool_calls', [])
        if not tool_calls:
            print("错误：没有找到工具调用")
            return {'messages': []}
        
        results = []
        for tool_call in tool_calls:
            print(f"正在调用工具: {tool_call}")
            
            try:
                tool_name = tool_call.get('name') or tool_call.get('function', {}).get('name')
                tool_args = tool_call.get('args') or tool_call.get('function', {}).get('arguments', {})
                tool_id = tool_call.get('id', 'unknown')
                
                if tool_name not in self.tools:
                    print(f"错误：未知的工具名称 '{tool_name}'")
                    result = f"错误：工具 '{tool_name}' 不存在，可用工具: {list(self.tools.keys())}"
                else:
                    # 执行工具
                    result = self.tools[tool_name].invoke(tool_args)
                    print(f"工具 '{tool_name}' 执行成功")
                
                # 创建工具消息
                tool_message = ToolMessage(
                    tool_call_id=tool_id,
                    name=tool_name,
                    content=str(result)
                )
                results.append(tool_message)
                
            except Exception as e:
                print(f"工具执行错误: {e}")
                error_tool_message = ToolMessage(
                    tool_call_id=tool_call.get('id', 'error'),
                    name=tool_call.get('name', 'unknown'),
                    content=f"工具执行失败: {str(e)}"
                )
                results.append(error_tool_message)
        
        print("返回到模型!")
        return {'messages': results}

prompt = """You are a smart research assistant. Use the search engine to look up information. \
You are allowed to make multiple calls (either together or in sequence). \
Only look up information when you are sure of what you want. \
If you need to look up some information before asking a follow up question, you are allowed to do that!
"""

tool = TavilySearchResults(max_results=4) #increased number of results


abot = Agent(llm, [tool], system=prompt)

result = abot.graph.invoke({"messages": [HumanMessage(content="What is the weather in sf?")]})

print("Final Result:")
for message in result['messages']:
    if isinstance(message, AIMessage):
        print(f"AI: {message.content}")
    elif isinstance(message, ToolMessage):
        print(f"Tool {message.name} returned: {message.content}")
    else:
        print(f"Unknown message type: {message}")
        print(message)