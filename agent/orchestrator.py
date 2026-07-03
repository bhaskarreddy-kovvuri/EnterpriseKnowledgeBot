import json
from datetime import date
from openai import OpenAI
from config.settings import OPENAI_API_KEY
from tools.tool_registry import TOOLS
from tools.tool_registry import CALCULATOR_TOOL, RAG_SEARCH_TOOL, WEATHER_TOOL, GMAIL_TOOL, EXPENSE_TOOL

client = OpenAI(api_key=OPENAI_API_KEY)

TODAY = date.today().isoformat()

SYSTEM_PROMPT = f"""
You are an Enterprise AI Knowledge Bot.
Today's date is: {TODAY}
Important Instructions:
1. Today's date is {TODAY}.
2. When calling tools:
- If the user says "today", use "{TODAY}".
- If the user says "yesterday", use one day before "{TODAY}".
- If the user specifies a date, preserve it.
- If no date is mentioned, do not invent one.
3. Always use tools whenever applicable.
4. Never answer from memory if a tool can provide the data.
5. All expenses are in INR.
"""

def ask(question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": question
            }
        ],
        tools=[CALCULATOR_TOOL, RAG_SEARCH_TOOL, WEATHER_TOOL, GMAIL_TOOL, EXPENSE_TOOL],
        tool_choice="auto"
    )

    message = response.choices[0].message

    # No tool call
    if not message.tool_calls:
        return message.content

    tool_call = message.tool_calls[0]
    tool_name = tool_call.function.name

    args = json.loads(
        tool_call.function.arguments
    )

    tool = TOOLS[tool_name]
    if tool_name == "rag_search":
        # For RAG search, we need to pass the question as well
        args["question"] = question
        result = tool.execute(
            args["question"]
        )
    elif tool_name == "weather":
        result = tool.execute(
            args["city"]
        )
    elif tool_name == "calculator":
        result = tool.execute(
            args["operation"],
            args["arguments"]
        )
    elif tool_name == "gmail_search":
        result = tool.execute(
            args
        )
    elif tool_name == "expense_tool":
        result = tool.execute(
            args
        )

    # Send tool result back to GPT
    final = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": question
        },
        message,
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        }
    ])
    return final.choices[0].message.content