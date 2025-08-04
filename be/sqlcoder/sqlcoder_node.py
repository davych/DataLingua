

from typing import Dict, Any
from state import State

class SQLCoderAgent:
    def __init__(self, model_client):
        self.model_client = model_client

    def __call__(self, state: State) -> State:
        nlu_result = state.get('nlu_result', '')
        result = self.model_client.generate_sql(nlu_result)
        state['sql'] = result
        return state
