from langchain_openai import OpenAIEmbeddings
from config.settings import OPENAI_API_KEY

def get_embedding_model():
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY
    )