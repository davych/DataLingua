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

    # Save the graph as a PNG file and display it
    graph = workflow.graph.get_graph()
    img =  graph.draw_mermaid_png()
    with open("workflow_graph.png", "wb") as f:
        f.write(img)

    # user_query = "我想看每个分类下有多少歌曲.我需要分类名称以及歌曲数量"
    # result = workflow.run(user_query)
    # print("=== Workflow Result ===")
    # print('user_query -', user_query)
    # print('translated -', result.get('nlu_result', ''))
    # print('sql -', result.get('sql', ''))