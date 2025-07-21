from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_ollama import ChatOllama
from db.connection import db
from langchain_core.messages import HumanMessage
# from langchain_core.prompts import ChatPromptTemplate
from prompt.common import system_message
from langgraph.prebuilt import create_react_agent


llm = ChatOllama(model="MFDoom/deepseek-r1-tool-calling:14b")

def main():
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()
    agent_executor = create_react_agent(llm, tools, prompt=system_message)
    question = "what the album name of artist Aerosmith?"
    message = HumanMessage(content=question)
    for step in agent_executor.stream(
        {"messages": [message]},
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()
if __name__ == "__main__":
    main()
