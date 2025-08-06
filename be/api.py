from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional, Generator
import uuid
from nlu.nlu_node import NLUAgent
from sqlcoder.sqlcoder_node import SQLCoderAgent
from db.db_service import DBService
from workflow import Workflow
from nlu.llm_azure import model
from sqlcoder.llm_sqlcoder import SqlCoderLLM
from service import DataLinguaService

app = FastAPI()

# 允许所有CORS，生产环境请收敛
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# sid -> [conversation_id1, conversation_id2, ...]
sid_conversation_map: Dict[str, list] = {}
# conversation_id -> context (可扩展为上下文对象)
conversation_context: Dict[str, dict] = {}

class QARequest(BaseModel):
    query: list[str]  # 消息历史，字符串数组
    conversation_id: str  # 必须由前端生成并传入


from fastapi import Cookie

@app.post("/qa")
def qa_endpoint(req: QARequest, sid: Optional[str] = Cookie(None)):
    # sid从cookie读取，conversation_id由前端传入
    conversation_id = req.conversation_id
    # 记录sid->conversation_id映射
    if sid:
        sid_conversation_map.setdefault(sid, []).append(conversation_id)
    # 每次新建 workflow
    nlu_agent = NLUAgent(model)
    sqlcoder_llm = SqlCoderLLM()
    sqlcoder_agent = SQLCoderAgent(sqlcoder_llm)
    db_service = DBService(db_path="Chinook.db")
    workflow = Workflow(nlu_agent, sqlcoder_agent, db_service)
    service = DataLinguaService(workflow)

    # 直接用query数组作为消息历史
    result = service.query_with_clarification(req.query)
    headers = {"X-Conversation-Id": conversation_id}

    print(f"Result: {result}")

    # if isinstance(result, dict) and result.get('needs_clarification'):
    #     return JSONResponse(content={
    #         "conversation_id": conversation_id,
    #         "needs_clarification": True,
    #         "follow_up": result.get('follow_up'),
    #         "nlu_result": result.get('nlu_result')
    #     })
    return JSONResponse(content={
            "conversation_id": conversation_id,
            "needs_clarification": result.get('needs_clarification', False),
            "context": [msg.content for msg in result.get('user_query', [])],
            "result": result.get('result'),
            "status": result.get('status', ''),
            "error": result.get('error', ''),
            "follow_up": result.get('follow_up'),
            "nlu_result": result.get('nlu_result')
        })

@app.get("/conversation_ids/{sid}")
def get_conversation_ids(sid: str):
    ids = sid_conversation_map.get(sid, [])
    return {"sid": sid, "conversation_ids": ids}

@app.get("/conversation_context/{conversation_id}")
def get_conversation_context(conversation_id: str):
    ctx = conversation_context.get(conversation_id, {})
    return ctx
