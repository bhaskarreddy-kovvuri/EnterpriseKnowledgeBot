from datetime import datetime
from models.expense import Expense
from services.expense_service import ExpenseService


class ExpenseTool:

    def __init__(self):
        self.service = ExpenseService()

    def execute(self, args):

        action = args.get("action")

        ############################################################
        # ADD EXPENSE
        ############################################################

        if action == "add_expense":
            expense = Expense(
                expense_category=args.get(
                    "expense_category",
                    "Others"
                ),
                expense_description=args.get(
                    "expense_description",
                    ""
                ),
                amount=float(args.get(
                    "amount",
                    0
                )),
                payment_mode=args.get(
                    "payment_mode",
                    "Unknown"
                ),
                bankname=args.get(
                    "bankname",
                    ""
                ),
                buy_from=args.get(
                    "buy_from",
                    ""
                ),
                date_bought=self.normalize_date(
                    args.get("date_bought")
                )
            )
            result = self.service.add_expense(
                expense
            )
            return {
                "status": "success",
                "message": "Expense added successfully.",
                "expense": result
            }

        ############################################################
        # SEARCH
        ############################################################

        elif action == "search":
            expenses = self.service.search(
                category=args.get(
                    "expense_category"
                ),
                payment_mode=args.get(
                    "payment_mode"
                ),
                bankname=args.get(
                    "bankname"
                ),
                buy_from=args.get(
                    "buy_from"
                ),
                start_date=args.get(
                    "start_date"
                ),
                end_date=args.get(
                    "end_date"
                ),
                min_amount=args.get(
                    "min_amount"
                ),
                max_amount=args.get(
                    "max_amount"
                )
            )

            return {
                "count": len(expenses),
                "expenses": expenses
            }

        ############################################################
        # TOTAL
        ############################################################

        elif action == "total_spending":
            return {
                "total": self.service.total_spending()
            }

        ############################################################
        # MONTH
        ############################################################

        elif action == "monthly_spending":
            return {
                "total": self.service.monthly_spending()
            }

        ############################################################
        # CATEGORY
        ############################################################

        elif action == "category_summary":
            return self.service.category_summary()

        ############################################################
        # MERCHANT
        ############################################################

        elif action == "top_merchant":
            return {
                "merchant": self.service.top_merchant()
            }

        ############################################################

        return {
            "status": "error",
            "message": "Unknown action."
        }

    def normalize_date(self,date_string):
        today = datetime.today().date()
        if not date_string:
            return today
        value = date_string.lower()
        print(f"Value: {value}")
        if value == "today":
            return today
        if value == "yesterday":
            return today - timedelta(days=1)
        return datetime.strptime(
            date_string,
            "%Y-%m-%d"
        ).date()  
        
