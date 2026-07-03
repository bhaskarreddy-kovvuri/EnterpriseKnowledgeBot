CALCULATOR_TOOL = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": (
            "Perform mathematical calculations. "
            "Use this tool whenever the user asks for arithmetic, "
            "percentages, square roots, powers, interest calculations, etc."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "enum": [
                        "add",
                        "subtract",
                        "multiply",
                        "divide",
                        "square_root",
                        "power",
                        "percentage",
                        "simple_interest",
                        "compound_interest"
                    ]
                },
                "arguments": {
                    "type": "object",
                    "description": "Arguments required for the selected operation."
                }
            },
            "required": [
                "operation",
                "arguments"
            ]
        }
    }
}

WEATHER_TOOL = {

    "type": "function",

    "function": {

        "name": "weather",

        "description": """
Retrieve the current real-time weather
for a city.

Use this tool whenever the user asks:

- weather
- temperature
- humidity
- rain
- wind
- climate
- today's weather
- current weather

Never answer from memory.
Always call this tool.
""",

        "parameters": {

            "type": "object",

            "properties": {

                "city": {

                    "type": "string",

                    "description": "City name"

                }

            },

            "required": [

                "city"

            ]

        }

    }

}

RAG_SEARCH_TOOL = {
    "type": "function",
    "function": {
        "name": "rag_search",
        "description": """
                Searches enterprise documents stored in the vector database.

                Use this tool whenever the user asks about

                - Market Analysis
                - Competitor Analysis
                - Marketing Strategy
                - Innovate Tech Solutions

                You are an AI Knowledge Assistant.
                
                Answer ONLY from the supplied context.
                If answer not available say
                "I don't know.
                """,
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "Question to search"
                }
            },

            "required": [
                "question"
            ]
        }
    }
}

EMAIL_TOOL = {

    "type": "function",

    "function": {

        "name": "email",

        "description": """
Retrieve onboarding and resignation statistics
from company emails.

Use this tool whenever the user asks:

- Aboard
- onboarding
- joining
- resignation
- offboarding
- employee joined
- employee resigned
- new hires
- exits
- attrition
- signoff
- adieu
- last working day

""",

        "parameters": {

            "type": "object",

            "properties": {

                "action": {

                    "type": "string",

                    "enum": [

                        "onboarding",

                        "resignation"

                    ]

                },

                "period": {

                    "type": "string",

                    "enum": [

                        "today",

                        "week",

                        "month"

                    ]

                }

            },

            "required": [

                "action",

                "period"

            ]

        }

    }

}

GMAIL_TOOL = {
    "type": "function",
    "function": {
        "name": "gmail_search",
        "description": """
Search the user's Gmail mailbox.

Use this tool whenever the user asks to search emails by:

- Subject
- Sender email
- Recipient email
- Body keywords
- Attachments
- Date range
- Unread emails
- Labels

Examples:
- Search emails with subject
- Find resignation emails
- Search emails from HR
- Find emails containing Invoice
- Show emails with PDF attachments
- Show unread emails from last week
""",
        "parameters": {
            "type": "object",
            "properties": {

                "subject": {
                    "type": "string",
                    "description": "Words expected in the email subject."
                },

                "from_email": {
                    "type": "string",
                    "description": "Sender email address."
                },

                "to_email": {
                    "type": "string",
                    "description": "Recipient email address."
                },

                "body_keywords": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Keywords expected inside the email body."
                },

                "has_attachment": {
                    "type": "boolean",
                    "description": "True if attachments are required."
                },

                "attachment_type": {
                    "type": "string",
                    "description": "Optional attachment type such as pdf, xlsx, pptx."
                },

                "unread_only": {
                    "type": "boolean"
                },

                "after_date": {
                    "type": "string",
                    "description": "YYYY-MM-DD"
                },

                "before_date": {
                    "type": "string",
                    "description": "YYYY-MM-DD"
                },

                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of emails.",
                    "default": 10
                }

            }
        }
    }
}

EXPENSE_TOOL = {

    "type": "function",

    "function": {

        "name": "expense_tool",

        "description": """
Manage household expenses.

Always use this tool whenever
the user wants to

• Add an expense
• Search expenses
• Calculate spending
• Monthly summary
• Category summary
• Merchant summary

Never calculate from memory.
Always use this tool.



Instructions:
1. All the expenses are in Indian Rupees (INR).
2. If any of the parameters are missing, the tool should work and take defaults.
3. Show the expense summary in Indian Rupees (INR).
4. Expense date in YYYY-MM-DD format.
    If the user says:
    today -> today's date
    yesterday -> yesterday's date
    last Monday -> convert to YYYY-MM-DD
    Always provide this field.

""",

        "parameters": {

            "type": "object",

            "properties": {

                "action": {

                    "type": "string",

                    "enum": [

                        "add_expense",

                        "search",

                        "total_spending",

                        "monthly_spending",

                        "category_summary",

                        "top_merchant"

                    ]

                },

                "expense_category": {

                    "type": "string"

                },

                "expense_description": {

                    "type": "string"

                },

                "amount": {

                    "type": "number"

                },

                "payment_mode": {

                    "type": "string"

                },

                "bankname": {

                    "type": "string"

                },

                "buy_from": {

                    "type": "string"

                },

                "date_bought": {

                    "type": "string",

                    "description": "YYYY-MM-DD"

                },

                "start_date": {

                    "type": "string"

                },

                "end_date": {

                    "type": "string"

                },

                "min_amount": {

                    "type": "number"

                },

                "max_amount": {

                    "type": "number"

                }

            },

            "required": [

                "action"

            ]

        }

    }

}