"""
用 LangGraph 实现的 DataLingua MVP Workflow。
- 串联 NLU 节点、SQLCoder agent、DB 查询节点。
- 结构与架构文档一致，便于后续扩展。
"""
from typing import Any, Dict
from langgraph.graph import StateGraph, END

# 假设已有 nlu_node, sqlcoder_agent, db_service 实现
from .nlu_node import NLUNode
from .sqlcoder_agent import SQLCoderAgent
from .db_service import DBService

class LangGraphWorkflow:
    def __init__(self, nlu_node: NLUNode, sqlcoder_agent: SQLCoderAgent, db_service: DBService):
        self.nlu_node = nlu_node
        self.sqlcoder_agent = sqlcoder_agent
        self.db_service = db_service
        self.graph = self._build_graph()

    def _build_graph(self):
        g = StateGraph()
        g.add_node('nlu', self._nlu_step)
        g.add_node('sqlcoder', self._sqlcoder_step)
        g.add_node('db', self._db_step)
        g.add_edge('nlu', 'sqlcoder')
        g.add_edge('sqlcoder', 'db')
        g.add_edge('db', END)
        g.set_entry('nlu')
        return g


    def _nlu_step(self, state: Dict[str, Any]) -> Dict[str, Any]:
        # 直接以 agent 方式调用
        return self.nlu_node(state)

    def _sqlcoder_step(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return self.sqlcoder_agent(state)

    def _db_step(self, state: Dict[str, Any]) -> Dict[str, Any]:
        result = self.db_service.query(state['sql'])
        state['result'] = result
        return state

    def run(self, user_query: str) -> Dict[str, Any]:
        state = {'user_query': user_query}
        return self.graph.run(state)
