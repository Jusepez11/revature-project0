class User:
    def __init__(self, id:int, username:str, password:str, role:str) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.role = role