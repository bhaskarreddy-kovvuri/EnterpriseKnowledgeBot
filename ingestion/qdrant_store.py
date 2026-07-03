from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from config.settings import *

def store_vectors(chunks,embedding):
    client=QdrantClient(
        host=QDRANT_HOST,
        port=QDRANT_PORT,
        timeout=120
    )

    vector_store=QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embedding,
        url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",
        collection_name=COLLECTION_NAME
    )

    return vector_store