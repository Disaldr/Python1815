class User:
    def __init__(self):
        self.login = None
        self.password = None
        self.id = 0

    def enter_login(self, login):
        if re.match(login//):
            self.login = login
        else:
            вы

    def enter_password(self):

    def greet(self):
        if self.login and self.password:
            self.id =



user = User()
user.enter_login(input("Введите логин"))
user.enter_password(input("Введите пароль"))
user.greet()