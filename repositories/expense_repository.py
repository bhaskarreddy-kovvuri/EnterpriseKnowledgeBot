from database.supabase_client import SupabaseClient
from models.expense import Expense


class ExpenseRepository:

    def __init__(self):
        self.db = SupabaseClient.get_client()

    #######################################################
    # INSERT
    #######################################################

    def add_expense(
        self,
        expense: Expense
    ):
        response = (
            self.db
            .table("household_expense")
            .insert(
                {
                    "expense_category":
                        expense.expense_category,
                    "expense_description":
                        expense.expense_description,
                    "amount":
                        expense.amount,
                    "payment_mode":
                        expense.payment_mode,
                    "bankname":
                        expense.bankname,
                    "buy_from":
                        expense.buy_from,
                    "date_bought":
                        expense.date_bought.isoformat()
                }
            )
            .execute()
        )

        return response.data

    #######################################################
    # GET ALL
    #######################################################

    def get_all(self):

        return (
            self.db
            .table("household_expense")
            .select("*")
            .order(
                "date_bought",
                desc=True
            )
            .execute()
            .data
        )

    #######################################################
    # DELETE
    #######################################################

    def delete(self, expense_id):
        return (
            self.db
            .table("household_expense")
            .delete()
            .eq(
                "id",
                expense_id
            )
            .execute()
        )

    #######################################################
    # UPDATE
    #######################################################

    def update(
        self,
        expense_id,
        values
    ):

        return (
            self.db
            .table("household_expense")
            .update(values)
            .eq(
                "id",
                expense_id
            )
            .execute()
        )
    
    def search(
        self,
        category=None,
        bankname=None,
        payment_mode=None,
        buy_from=None,
        start_date=None,
        end_date=None,
        min_amount=None,
        max_amount=None,
        limit=100
    ):

        query = (
            self.db
            .table("household_expense")
            .select("*")
        )

        if category:
            query = query.eq(
                "expense_category",
                category
            )

        if bankname:
            query = query.eq(
                "bankname",
                bankname
            )

        if payment_mode:
            query = query.eq(
                "payment_mode",
                payment_mode
            )

        if buy_from:
            query = query.ilike(
                "buy_from",
                f"%{buy_from}%"
            )

        if start_date:
            query = query.gte(
                "date_bought",
                start_date
            )

        if end_date:
            query = query.lte(
                "date_bought",
                end_date
            )

        if min_amount is not None:
            query = query.gte(
                "amount",
                min_amount
            )

        if max_amount is not None:
            query = query.lte(
                "amount",
                max_amount
            )

        return (
            query
            .order(
                "date_bought",
                desc=True
            )
            .limit(limit)
            .execute()
            .data
        )

