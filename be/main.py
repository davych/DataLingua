from typing import Any, Dict, Optional
from nlu.nlu_node import NLUAgent
from sqlcoder.sqlcoder_node import SQLCoderAgent
from db.db_service import DBService
from workflow import Workflow
from nlu.llm_client import llm
from sqlcoder.llm_sqlcoder import SqlCoderLLM

from service import DataLinguaService

if __name__ == "__main__":
    nlu_agent = NLUAgent(llm)
    sqlcoder_llm = SqlCoderLLM()
    sqlcoder_agent = SQLCoderAgent(sqlcoder_llm)
    db_service = DBService(db_path=":memory:")  # 用内存数据库演示

    workflow = Workflow(nlu_agent, sqlcoder_agent, db_service)

    # Save the graph as a PNG file and display it
    # graph = workflow.graph.get_graph()
    # img =  graph.draw_mermaid_png()
    # with open("workflow_graph.png", "wb") as f:
    #     f.write(img)

    service = DataLinguaService(workflow)
    original_user_query = "我要看歌手和专辑的分布"
    result = service.query_with_clarification(original_user_query)
    from pprint import pprint
    print("=== Workflow Result ===")
    pprint(result)
   