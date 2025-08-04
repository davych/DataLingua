from typing import Any, Dict, List, Optional, TypedDict, Union
from langgraph.graph import  END

from langchain_core.messages import BaseMessage
class State(TypedDict, total=False):
    user_query: List[BaseMessage]
    nlu_result: Dict[str, Any]
    sql: str
    result: Any
    status: str
    error: str
    needs_clarification: bool
    follow_up_question: Optional[str]