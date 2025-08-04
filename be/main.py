from nlu.nlu_node import NLUAgent
from sqlcoder.sqlcoder_node import SQLCoderAgent
from db.db_service import DBService
from workflow import Workflow
from nlu.llm_client import llm
from sqlcoder.llm_sqlcoder import SqlCoderLLM


class MockSQLCoder:
    def generate_sql(self, prompt):
        return "SELECT region, SUM(sales) FROM sales_table WHERE year=2023 GROUP BY region;"

if __name__ == "__main__":
    nlu_agent = NLUAgent(llm)
    sqlcoder_llm = SqlCoderLLM()
    sqlcoder_agent = SQLCoderAgent(sqlcoder_llm)
    db_service = DBService(db_path=":memory:")  # 用内存数据库演示

    workflow = Workflow(nlu_agent, sqlcoder_agent, db_service)

    user_query = "I'd like to see a summary of album-artist distribution"
    import json
    result = workflow.run(user_query)
    print("=== Workflow Result ===")
    print(result,json.dumps(result, indent=2, ensure_ascii=False))
