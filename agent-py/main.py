# src/main.py
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json

from agent.sql_agent import sql_agent
from langchain_core.messages import HumanMessage

class QueryRequest(BaseModel):
    question: str

app = FastAPI(title="SQL Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


agent_executor = sql_agent()

@app.get("/")
def root():
    return {"message": "SQL Agent API"}

@app.post("/query")
def query(request: QueryRequest):
    result = agent_executor.invoke({
        "messages": [HumanMessage(content=request.question)]
    })
    
    last_message = result["messages"][-1]
    return {"answer": last_message.content}

@app.post("/query/stream")
def query_stream(request: QueryRequest):
    def generate():
        for step in agent_executor.stream(
            {"messages": [HumanMessage(content=request.question)]},
            stream_mode="values"
        ):  
            if step.get("messages"):
                last_message = step["messages"][-1]
                last_message.pretty_print()
                data = {
                    "type": type(last_message).__name__,
                    "content": getattr(last_message, 'content', ''),
                }
                
                if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
                    data["tool_calls"] = last_message.tool_calls
                
                yield f"data: {json.dumps(data)}\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)