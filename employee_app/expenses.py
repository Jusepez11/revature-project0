from __future__ import annotations
import db.db
class Expense:
    def __init__(self, id:int, user_id:int, amount:int, description:str, date:str) -> None:
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.description = description
        self.date = date


    def create(self, expense:Expense):
        conn = db.get_connection()
        cursor = conn.execute(
            """
            INSERT INTO expenses (user_id, amount, description, date)
            VALUES (?, ?, ?, ?)
            """,
            (expense.user_id, expense.amount, expense.description, expense.date)
        )

        expense.id = cursor.lastrowid
        conn.close()

        return expense
    
    def get_all(self):
        conn = db.get_connection()
        cursor = conn.execute(
            """
            SELECT * FROM expenses
            """
        )

        rows = cursor.fetchall()
        expenses = []

        for row in rows:
            expenses.append(Expense(
                id=row[0],
                user_id=row[1],
                amount=row[2],
                description=row[3],
                date=row[4]
            ))

        conn.close()

        return expenses

    def get_from_id(self,id:int):
        conn = db.get_connection()
        cursor = conn.execute(
        """
        SELECT * FROM expenses WHERE id = ?
        """, 
        (id,)
        )
    
        row = cursor.fetchone()

        if row is None:
            return None

        return Expense(
                id=row[0],
                user_id=row[1],
                amount=row[2],
                description=row[3],
                date=row[4]
        )


