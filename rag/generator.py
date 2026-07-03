from langchain_openai import ChatOpenAI
from config.settings import *

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY,
    temperature=0
)


def generate(prompt):
    response = llm.invoke(prompt)
    return response.content