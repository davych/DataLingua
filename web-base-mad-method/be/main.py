

from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

from db import SessionLocal, init_db
from llm_client import nl_to_sql
from chart import recommend_chart
import asyncio
from contextlib import asynccontextmanager
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# 允许所有 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query(request: QueryRequest):
    sql = await nl_to_sql(request.question)
    if not sql:
        raise HTTPException(status_code=400, detail="LLM未能生成SQL")
    db = SessionLocal()
    try:
        result = db.execute(text(sql))
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result.fetchall()]
    except Exception as e:
        db.close()
        raise HTTPException(status_code=400, detail=f"SQL执行失败: {e}")
    db.close()
    chart_types = recommend_chart(sql, data)
    return {"data": data, "chartTypes": chart_types}

# uvicorn main:app --reload --host 0.0.0.0 --port 8000

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)