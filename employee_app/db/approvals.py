from __future__ import annotations
import db
class Approval:
    def __init__(self, id:int, expense_id:int, status:str, reviewer:int, comment:str, review_date:str) -> None:
        self.id = id
        self.expense_id = expense_id
        self.status = status
        self.reviewer = reviewer
        self.comment = comment
        self.review_date = review_date


    def create(self, approval:Approval):
        conn = db.get_connection()
        cursor = conn.execute(
            """
            INSERT INTO approvals (expense_id, status, reviewer, comment, review_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (approval.expense_id, approval.status, approval.reviewer, approval.comment, approval.review_date)
        )

        approval.id = cursor.lastrowid
        conn.close()

        return approval
    
    def get_all(self):
        conn = db.get_connection()
        cursor = conn.execute(
            """
            SELECT * FROM approvals
            """
        )

        rows = cursor.fetchall()
        approvals = []

        for row in rows:
            approvals.append(Approval(
                id= row[0],
                expense_id=row[1],
                status=row[2],
                reviewer=row[3],
                comment=row[4],
                review_date=row[5]
            ))

        conn.close()

        return approvals

    def get_from_id(self,id:int):
        conn = db.get_connection()
        cursor = conn.execute(
        """
        SELECT * FROM approvals WHERE id = ?
        """, 
        (id,)
        )
    
        row = cursor.fetchone()

        if row is None:
            return None

        return Approval(
                id= row[0],
                expense_id=row[1],
                status=row[2],
                reviewer=row[3],
                comment=row[4],
                review_date=row[5]
        )


