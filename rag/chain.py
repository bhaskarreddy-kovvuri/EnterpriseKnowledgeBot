from rag.retriever import retrieve
from rag.prompt import build_prompt
from rag.generator import generate
from agent.planner import decide_tool
from agent.executor import execute


def ask(question):
    tool_name = decide_tool(question)
    if tool_name:
        return execute(tool_name, question)

    docs = retrieve(question)
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = build_prompt(
        context,
        question
    )

    answer = generate(prompt)
    return answer