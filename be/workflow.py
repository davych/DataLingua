
from typing import Any, Dict, TypedDict
from langgraph.graph import StateGraph, END
from state import State

class Workflow:
    def __init__(self, nlu_agent, sqlcoder_agent, db_service):
        self.nlu_agent = nlu_agent
        self.sqlcoder_agent = sqlcoder_agent
        self.db_service = db_service
        self.graph = self._build_graph()

    def _build_graph(self):
        g = StateGraph(State)
        g.add_node('nlu', self._nlu_step)
        g.add_node('sqlcoder', self._sqlcoder_step)
        g.add_node('db', self._db_step)
        g.add_edge('nlu', 'sqlcoder')
        g.add_edge('sqlcoder', 'db')
        g.add_edge('db', END)
        g.set_entry_point('nlu')
        return g.compile()

    def _nlu_step(self, state: State, config=None) -> State:
        result = self.nlu_agent(state)
        return result

    def _sqlcoder_step(self, state: State, config=None) -> State:
        return self.sqlcoder_agent(state)

    def _db_step(self, state: State, config=None) -> State:
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
        state: State = {
            'user_query': user_query,
            'nlu_result': '',
            'sql': '',
            'result': None,
            'status': '',
            'error': ''
        }
        return self.graph.invoke(state)
