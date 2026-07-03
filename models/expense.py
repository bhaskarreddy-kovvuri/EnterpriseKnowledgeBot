from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    expense_category: str
    expense_description: str
    amount: float
    payment_mode: str
    bankname: str
    buy_from: str
    date_bought: date