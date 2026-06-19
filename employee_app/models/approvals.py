class Approval:
    def __init__(self, id:int, expense_id:int, status:str, reviewer:int, comment:str, review_date:str) -> None:
        self.id = id
        self.expense_id = expense_id
        self.status = status
        self.reviewer = reviewer
        self.comment = comment
        self.review_date = review_date
