from langchain_community.document_loaders import PyMuPDFLoader
import os

def load_documents(folder):
    documents=[]
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            loader = PyMuPDFLoader(
                os.path.join(folder, file)
            )
            documents.extend(loader.load())
    return documents