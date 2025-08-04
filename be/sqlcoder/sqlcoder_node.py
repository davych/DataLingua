

from typing import Dict, Any
from state import State

class SQLCoderAgent:
    def __init__(self, model_client):
        self.model_client = model_client

    def __call__(self, state: State) -> State:
        nlu_result = state.get('nlu_result', {})
        # get translation
        query = nlu_result.get('translation', '')
        related_tables = nlu_result.get('related_tables', [])

        query += f". related tables: {', '.join(related_tables)}" if related_tables else ""

        print(f"Generating SQL for query: {query}")
        result = self.model_client.generate_sql(query)
        print(f"Generated SQL: {result}")
        state['sql'] = result
        return state
