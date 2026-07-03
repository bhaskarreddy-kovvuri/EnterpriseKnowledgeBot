from tools.calculator import Calculator
from tools.weather import WeatherTool 
from tools.rag_search import RagSearchTool
from tools.gmail_tool import GmailTool
from tools.expense_tool import ExpenseTool
from tools.tool_definitions import *

calculator = Calculator()
rag = RagSearchTool()
weather = WeatherTool()
gmail = GmailTool()
expense = ExpenseTool()

TOOLS = {
    "calculator": calculator,
    "weather": weather,
    "rag_search": rag,
    "gmail_search": gmail,
    "expense_tool": expense
}

TOOL_DEFINITIONS = [
    CALCULATOR_TOOL,
    RAG_SEARCH_TOOL,
    GMAIL_TOOL,
    WEATHER_TOOL,
    EXPENSE_TOOL
]