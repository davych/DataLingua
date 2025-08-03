
"""
LangGraph Workflow 主流程实现：严格遵循 langgraph StateGraph/add_node/add_edge/set_entry。
"""
from typing import Any, Dict
from langgraph.graph import StateGraph, END

class Workflow:
    def __init__(self, nlu_agent, sqlcoder_agent, db_service):
        self.nlu_agent = nlu_agent
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
        # nlu_agent 必须是 langgraph agent（如 create_react_agent 返回值）
        return self.nlu_agent(state)

    def _sqlcoder_step(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return self.sqlcoder_agent(state)

    def _db_step(self, state: Dict[str, Any]) -> Dict[str, Any]:
        sql = state.get('sql')
        try:
            result = self.db_service.query(sql)
            state['result'] = result
            state['status'] = 'success'
        except Exception as e:
            state['result'] = None
            state['status'] = 'db_query_failed'
            state['error'] = str(e)
        return state

    def run(self, user_query: str) -> Dict[str, Any]:
        state = {'user_query': user_query}
        return self.graph.run(state)
