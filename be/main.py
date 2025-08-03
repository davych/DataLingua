"""
主入口：演示如何初始化 NLU/SQLCoder agent 和 Workflow，并运行一次完整流程。
"""
from nlu_node import build_nlu_react_agent
from be.sqlcoder_node import SQLCoderAgent
from db_service import DBService
from workflow import Workflow

# 假设有支持 function/tool calling 的 LLM 和 SQLCoder model_client
# 这里用 mock 对象占位，实际部署时替换为真实模型
class MockLLM:
    def __call__(self, *args, **kwargs):
        return "{""intent"": ""query_data"", ""entities"": {""metrics"": [""销售额""], ""dimensions"": [""区域""], ""time_range"": ""2023年"", ""filters"": null}, ""missing_entities"": [], ""clarification_question"": null}"

class MockSQLCoder:
    def generate_sql(self, prompt):
        return "SELECT region, SUM(sales) FROM sales_table WHERE year=2023 GROUP BY region;"

if __name__ == "__main__":
    # 初始化 agent
    llm = MockLLM()
    nlu_agent = build_nlu_react_agent(llm)
    sqlcoder_agent = SQLCoderAgent(MockSQLCoder(), db_schema="sales_table schema ...")
    db_service = DBService(db_path=":memory:")  # 用内存数据库演示

    # 初始化 workflow
    workflow = Workflow(nlu_agent, sqlcoder_agent, db_service)

    # 用户输入
    user_query = "2023年各区域销售额"
    result = workflow.run(user_query)
    print("=== Workflow Result ===")
    print(result)
