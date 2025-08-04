"""
主入口：演示如何初始化 NLU/SQLCoder agent 和 Workflow，并运行一次完整流程。
"""
from nlu_node import NLUAgent
from sqlcoder_node import SQLCoderAgent
from db_service import DBService
from workflow import Workflow
from state import State
from llm_client import llm


class MockSQLCoder:
    def generate_sql(self, prompt):
        return "SELECT region, SUM(sales) FROM sales_table WHERE year=2023 GROUP BY region;"

if __name__ == "__main__":
    nlu_agent = NLUAgent(llm)
    sqlcoder_agent = SQLCoderAgent(MockSQLCoder(), db_schema="sales_table schema ...")
    db_service = DBService(db_path=":memory:")  # 用内存数据库演示

    workflow = Workflow(nlu_agent, sqlcoder_agent, db_service)

    user_query = "2023年各区域销售额"
    result = workflow.run(user_query)
    print("=== Workflow Result ===")
    print(result)
