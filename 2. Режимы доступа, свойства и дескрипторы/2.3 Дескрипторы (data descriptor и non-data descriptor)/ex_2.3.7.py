class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if type(string) is not str:
            return False
        if (len(string) < self.min_length) or (len(string) > self.max_length):
            return False
        else:
            return True

class StringValue:
    """
    Дескриптор данных
    """
    def __init__(self, validator=ValidateString(3, 100)):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self.name] = value

class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()
    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        str_out = f"""<form>\nЛогин: <{self.login}>\nПароль: <{self.password}>\nEmail: <{self.email}>\n</form>"""
        print(str_out)


r = RegisterForm('1111', '1111111', '11111111')
r.show()
v = ValidateString(5, 10)
assert v.validate("hello"), "метод validate вернул неверное значение"
assert v.validate("hell") == False, "метод validate вернул неверное значение"
assert v.validate("hello world") == False, "метод validate вернул неверное значение"