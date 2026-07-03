from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

from config.settings import *

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY
)

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding,
    url="http://"+QDRANT_HOST+":"+str(QDRANT_PORT),
    collection_name=COLLECTION_NAME
)


def retrieve(question):
    docs = vector_store.similarity_search(
        question,
        k=2
    )
    return docs