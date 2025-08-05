from typing import Any, Dict, Optional
from langchain_core.messages import HumanMessage, SystemMessage


class DialogueContext:
    def __init__(self, query_history):
        if  isinstance(query_history, list):
            self.messages = [HumanMessage(content=q) for q in query_history]
        else:
            raise ValueError("query_history must be str or list[str]")
    def append_user(self, user_input: str):
        self.messages.append(HumanMessage(content=user_input))

class DataLinguaService:
    def __init__(self, workflow):
        self.workflow = workflow
    
    def query_with_clarification(self, user_query) -> Dict[str, Any]:
        ctx = DialogueContext(user_query)
        while True:
            result = self.workflow.run(ctx.messages)
            nlu_result = result.get('nlu_result', {})
            if result.get('needs_clarification'):
                follow_up = nlu_result.get('follow_up_question', '请补充说明：')
                # 在API模式下，直接返回需要clarification的提示和上下文，不阻塞
                return {
                    'needs_clarification': True,
                    'follow_up': follow_up,
                    'context': ctx.messages,
                    'nlu_result': nlu_result
                }
            return result
    
    # def continue_query(self, ctx: DialogueContext, user_input: str, context_id: Optional[str] = None) -> Dict[str, Any]:
    #     ctx.append_user(user_input)
    #     messages = ctx.as_state()
    #     return self.workflow.run(messages, context_id=context_id)
