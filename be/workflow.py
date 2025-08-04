
from typing import Any, Dict, List, Optional, TypedDict
from langgraph.graph import StateGraph, END
from state import State
from langchain_core.messages import BaseMessage

class Workflow:
    def __init__(self, nlu_agent, sqlcoder_agent, db_service):
        self.nlu_agent = nlu_agent
        self.sqlcoder_agent = sqlcoder_agent
        self.db_service = db_service
        self.graph = self._build_graph()

    def _build_graph(self):
        g = StateGraph(State)
        
        # Add nodes
        g.add_node('nlu', self._nlu_step)
        g.add_node('sqlcoder', self._sqlcoder_step)
        g.add_node('db', self._db_step)
        
        def needs_clarification(state: State) -> bool:
            if state.get('needs_clarification', False):
                return True  # needs_clarification=True 时结束 workflow，不再循环
            else:
                return False  # 继续到 sqlcoder
        
        
        # Add edges for the workflow
        g.add_node('branch', lambda state: state)
        g.add_edge('nlu', 'branch')
        # @todo 不知道这里是不是best practice，需要继续刷文档了解
        g.add_conditional_edges('branch', needs_clarification, {True: END, False: 'sqlcoder'})
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

    def run(self, message: List[BaseMessage]) -> Dict[str, Any]:
        state: State = {
            'user_query': message,  # 使用合并后的完整查询
            'nlu_result': {},  # 重新开始，不传入历史 nlu_result
            'sql': '',
            'result': None,
            'status': '',
            'error': '',
            'needs_clarification': False,
            'follow_up_question': None
        }
        return self.graph.invoke(state)
