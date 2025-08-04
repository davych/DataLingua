from typing import Any, Dict, Optional
from langchain_core.messages import HumanMessage, SystemMessage

class DialogueContext:
    def __init__(self, initial_query: str):
        humanMsg = HumanMessage(content=initial_query)
        self.messages = [
            humanMsg
        ]
        self.original_query = humanMsg
    
    def append_user(self, user_input: str):
        self.messages.append(HumanMessage(content=user_input))

class DataLinguaService:
    def __init__(self, workflow):
        self.workflow = workflow
    
    def query_with_clarification(self, user_query: str) -> Dict[str, Any]:
        ctx = DialogueContext(user_query)
        while True:
            result = self.workflow.run(ctx.messages)
            nlu_result = result.get('nlu_result', {})
            if result.get('needs_clarification'):
                follow_up = nlu_result.get('follow_up_question', '请补充说明：')
                user_input = input(f"{follow_up}\n> ")
                ctx.append_user(user_input)
                continue
            return result
    
    # def continue_query(self, ctx: DialogueContext, user_input: str, context_id: Optional[str] = None) -> Dict[str, Any]:
    #     ctx.append_user(user_input)
    #     messages = ctx.as_state()
    #     return self.workflow.run(messages, context_id=context_id)
