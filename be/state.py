from typing import Any, Dict, TypedDict
from langgraph.graph import  END

class State(TypedDict):
    user_query: str
    nlu_result: Dict[str, Any]
    sql: str
    result: Any
    status: str
    error: str