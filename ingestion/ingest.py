from .loader import load_documents
from .splitter import split_documents
from .metadata import enrich_metadata
from .embeddings import get_embedding_model
from .qdrant_store import store_vectors

def run():
    print("Loading PDFs...")
    docs=load_documents("documents")
    print(len(docs))

    print("Chunking...")
    chunks=split_documents(docs)
    print(len(chunks))

    chunks=enrich_metadata(chunks)

    print("Embedding Model...")
    embedding=get_embedding_model()

    print("Uploading to Qdrant...")
    store_vectors(chunks,embedding)

    print("Completed")

if __name__=="__main__":
    run()