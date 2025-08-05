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
from nlu.llm_client import llm
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
    sid: str
    query: list[str]  # 消息历史，字符串数组
    conversation_id: Optional[str] = None



@app.post("/qa")
def qa_endpoint(req: QARequest):
    # 1. conversation_id 生成/复用（仅用于header，后端不再管理上下文）
    if req.conversation_id:
        conversation_id = req.conversation_id
    else:
        conversation_id = str(uuid.uuid4())
    # 2. 每次新建 workflow
    nlu_agent = NLUAgent(llm)
    sqlcoder_llm = SqlCoderLLM()
    sqlcoder_agent = SQLCoderAgent(sqlcoder_llm)
    db_service = DBService(db_path=":memory:")
    workflow = Workflow(nlu_agent, sqlcoder_agent, db_service)
    service = DataLinguaService(workflow)

    # 直接用query数组作为消息历史
    result = service.query_with_clarification(req.query)
    headers = {"X-Conversation-Id": conversation_id}

    print(f"Result: {result}")

    if isinstance(result, dict) and result.get('needs_clarification'):
        return JSONResponse(content={
            "conversation_id": conversation_id,
            "needs_clarification": True,
            "follow_up": result.get('follow_up'),
            "nlu_result": result.get('nlu_result')
        }, headers=headers) 
        
    def gen():
        yield str(result)
    return StreamingResponse(gen(), media_type="text/plain", headers=headers)

@app.get("/conversation_ids/{sid}")
def get_conversation_ids(sid: str):
    ids = sid_conversation_map.get(sid, [])
    return {"sid": sid, "conversation_ids": ids}

@app.get("/conversation_context/{conversation_id}")
def get_conversation_context(conversation_id: str):
    ctx = conversation_context.get(conversation_id, {})
    return ctx
