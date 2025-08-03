

"""
SQLCoder Agent 节点实现：标准 Python callable，兼容 LangGraph/StateGraph add_node。
"""
from typing import Dict, Any
from state import State

class SQLCoderAgent:
    def __init__(self, model_client, db_schema: str):
        """
        model_client: 负责与 SQLCoder 大模型通信的对象，需实现 generate_sql 接口。
        db_schema: 当前数据库 schema 字符串。
        """
        self.model_client = model_client
        self.db_schema = db_schema

    def __call__(self, state: State) -> State:
        nlu_result = state.get('nlu_result', {})
        entities = nlu_result.get('entities', {})
        prompt = f"""### Task\nGenerate a SQL query based on the natural language question and database schema.\n\n### Database Schema\n{self.db_schema}\n\n### Extracted Information\n- Metrics: {entities.get('metrics', [])}\n- Dimensions: {entities.get('dimensions', [])}\n- Time Range: {entities.get('time_range', 'N/A')}\n- Filters: {entities.get('filters', [])}\n\n### Requirements\n- Generate only SELECT statements\n- Use proper table joins if needed\n- Apply time filters based on time_range\n- Group by dimensions if specified\n- Aggregate metrics appropriately\n\n### SQL Query\nSELECT"""
        sql = self.model_client.generate_sql(prompt)
        state['sql'] = sql
        return state
