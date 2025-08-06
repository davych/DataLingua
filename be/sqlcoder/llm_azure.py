from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI

from dotenv import load_dotenv
load_dotenv()

deployment_name = "gpt-4o-mini-2024-07-18"

model = AzureChatOpenAI(
    azure_deployment=deployment_name,
    api_version="2024-02-01",  # or your api version
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
