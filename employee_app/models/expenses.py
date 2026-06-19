class Expense:
    def __init__(self, id:int, user_id:int, amount:int, description:str, date:str) -> None:
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.description = description
        self.date = date
