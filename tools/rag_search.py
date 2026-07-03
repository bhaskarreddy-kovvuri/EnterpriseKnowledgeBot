from rag.retriever import retrieve

class RagSearchTool:
    def execute(self, question: str):
        docs = retrieve(question)
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )
        return context