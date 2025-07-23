from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_ollama import ChatOllama
from db.connection import db
from prompt.common import system_message
from langgraph.prebuilt import create_react_agent


llm = ChatOllama(model="llama3.1:latest", temperature=0.1)

def sql_agent():
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()
    agent_executor = create_react_agent(llm, tools, prompt=system_message)
    return agent_executor
   