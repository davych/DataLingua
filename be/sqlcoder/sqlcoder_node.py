

from typing import Dict, Any
from state import State

class SQLCoderAgent:
    def __init__(self, model_client):
        """
        model_client: 负责与 SQLCoder 大模型通信的对象，需实现 generate_sql 接口。
        db_schema: 当前数据库 schema 字符串。
        """
        self.model_client = model_client

    def __call__(self, state: State) -> State:
        nlu_result = state.get('nlu_result', {})
        entities = nlu_result.get('entities', {})
        user_query = state.get('user_query', '')
        info_lines = []
        if entities.get('metrics'):
            info_lines.append(f"Metrics: {entities.get('metrics')}")
        if entities.get('dimensions'):
            info_lines.append(f"Dimensions: {entities.get('dimensions')}")
        if entities.get('time_range'):
            info_lines.append(f"Time Range: {entities.get('time_range')}")
        if entities.get('filters'):
            info_lines.append(f"Filters: {entities.get('filters')}")
        info_str = '\n'.join(info_lines)
        q = f"""{user_query} belows are my information:
            {info_str}
            """
        print(f"SQLCoder prompt: {q}")  # Debugging output
        result = self.model_client.generate_sql(q)
        state['sql'] = result
        return state
