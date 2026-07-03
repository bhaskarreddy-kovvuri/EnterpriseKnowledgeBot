from datetime import date, timedelta
from models.expense import Expense
from repositories.expense_repository import ExpenseRepository

class ExpenseService:

    def __init__(self):
        self.repository = ExpenseRepository()

    ####################################################
    # ADD EXPENSE
    ####################################################

    def add_expense(self, expense: Expense):
        self.validate(expense)
        expense.expense_category = self.normalize_category(
            expense.expense_category
        )
        expense.payment_mode = self.normalize_payment_mode(
            expense.payment_mode
        )
        return self.repository.add_expense(expense)

    ####################################################
    # VALIDATION
    ####################################################

    def validate(self, expense: Expense):
        if expense.amount <= 0:
            raise Exception(
                "Expense amount must be greater than zero."
            )

        if not expense.expense_category:
            raise Exception(
                "Expense category is mandatory."
            )

        if not expense.date_bought:
            raise Exception(
                "Expense date is mandatory."
            )

    ####################################################
    # CATEGORY NORMALIZATION
    ####################################################

    def normalize_category(self, category):

        mapping = {
            "grocery": "Groceries",
            "groceries": "Groceries",
            "medical": "Medical",
            "medicine": "Medical",
            "fuel": "Fuel",
            "petrol": "Fuel"
        }

        return mapping.get(
            category.lower(),
            category.title()
        )

    ####################################################
    # PAYMENT MODE NORMALIZATION
    ####################################################

    def normalize_payment_mode(self, payment):
        mapping = {
            "upi": "UPI",
            "cash": "Cash",
            "credit": "Credit Card",
            "credit card": "Credit Card",
            "debit": "Debit Card",
            "debit card": "Debit Card"
        }

        return mapping.get(
            payment.lower(),
            payment.title()
        )

    ####################################################
    # GET ALL
    ####################################################

    def get_all_expenses(self):
        return self.repository.get_all()

    ####################################################
    # SEARCH
    ####################################################

    def search(self, **kwargs):
        return self.repository.search(**kwargs)

    def total_spending(self):
        expenses = self.repository.get_all()
        return sum(
            float(x["amount"])
            for x in expenses
        )
    
    def monthly_spending(self):
        today = date.today()
        expenses = self.repository.search(
            start_date=today.replace(day=1)
        )
        return sum(
            float(x["amount"])
            for x in expenses
        )

    def category_summary(self):
        expenses = self.repository.get_all()
        summary = {}
        for expense in expenses:
            category = expense["expense_category"]
            summary.setdefault(category, 0)
            summary[category] += float(
                expense["amount"]
            )
        return summary

    def top_merchant(self):
        expenses = self.repository.get_all()
        merchants = {}
        for expense in expenses:
            merchant = expense["buy_from"]
            merchants.setdefault(merchant, 0)
            merchants[merchant] += float(
                expense["amount"]
            )
        if not merchants:
            return None
        return max(
            merchants,
            key=merchants.get
        )