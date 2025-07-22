from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_ollama import ChatOllama
from db.connection import db
from langchain_core.messages import HumanMessage
# from langchain_core.prompts import ChatPromptTemplate
from prompt.common import system_message
from langgraph.prebuilt import create_react_agent


llm = ChatOllama(model="MFDoom/deepseek-r1-tool-calling:14b")

def sql_agent():
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()
    agent_executor = create_react_agent(llm, tools, prompt=system_message)
    # message = HumanMessage(content=question)
    return agent_executor
   
