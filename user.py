class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


class Admin(User):
    def __init__(self, _id, username, password):
        super().__init__(_id, username, password)
        self.role = 'superadmin'


class Test_func:
    id = 2
    def __init__(self, id) -> None:
        self.id = id
    
    def square(self):
        return self.id * self.id
    
    @classmethod
    def summ(cls, another):
        if isinstance(another, Test_func):
            return cls.id + another.id