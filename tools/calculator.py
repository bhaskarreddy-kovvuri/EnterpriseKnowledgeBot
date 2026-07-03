# def calculate(expression: str) -> str:
#     try:
#         result = eval(expression, {"__builtins__": {}}, {})
#         return f"Result = {result}"
#     except Exception as ex:
#         return f"Calculation Error: {ex}"


import math


class Calculator:

    def execute(self, operation: str, arguments: dict):

        if operation == "add":
            return arguments["a"] + arguments["b"]

        elif operation == "subtract":
            return arguments["a"] - arguments["b"]

        elif operation == "multiply":
            return arguments["a"] * arguments["b"]

        elif operation == "divide":
            return arguments["a"] / arguments["b"]

        elif operation == "square_root":
            return math.sqrt(arguments["number"])

        elif operation == "power":
            return math.pow(
                arguments["base"],
                arguments["exponent"]
            )

        elif operation == "percentage":
            return (
                arguments["percentage"]
                * arguments["value"]
            ) / 100

        elif operation == "simple_interest":

            return (
                arguments["principal"]
                * arguments["rate"]
                * arguments["time"]
            ) / 100

        elif operation == "compound_interest":

            return (
                arguments["principal"]
                * (
                    1 + arguments["rate"] / 100
                ) ** arguments["time"]
            )

        else:
            raise Exception(
                f"Unsupported operation {operation}"
            )