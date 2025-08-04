

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
        metrics = entities.get('metrics')
        dimensions = entities.get('dimensions')
        # 优化自然语言提示，支持多个 metrics/dimensions
        metrics_str = ', '.join(metrics) if metrics else ''
        dimensions_str = ', '.join(dimensions) if dimensions else ''
        if metrics and dimensions:
            info_lines.append(f"Please help to {metrics_str} around different {dimensions_str}.")
        elif metrics:
            info_lines.append(f"Please help to {metrics_str}.")
        elif dimensions:
            info_lines.append(f"Please focus on different {dimensions_str} .")
        if entities.get('time_range'):
            info_lines.append(f"Time Range: {entities.get('time_range')}")
        if entities.get('filters'):
            info_lines.append(f"Filters: {entities.get('filters')}")
        info_str = '\n'.join(info_lines)
        q = f"""{user_query}\n{info_str}\n"""
        print(f"SQLCoder prompt: {q}")  # Debugging output
        result = self.model_client.generate_sql(user_query)
        state['sql'] = result
        return state
