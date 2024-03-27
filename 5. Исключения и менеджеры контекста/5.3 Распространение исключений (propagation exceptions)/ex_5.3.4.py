class ValidatorString(object):
    """docstring for ValidatorString."""

    def __init__(self, min_length, max_length, chars=""):
        super(ValidatorString, self).__init__()
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if self.chars == "":
            if len(string) < self.min_length or len(string) > self.max_length:
                raise ValueError("недопустимая строка")
        else:
            if (
                len(string) < self.min_length
                or len(string) > self.max_length
                or len(set(self.chars) - set(string)) == len(self.chars)
            ):
                raise ValueError("недопустимая строка")


class LoginForm(object):
    """docstring for LoginForm."""

    def __init__(self, login_validator, password_validator):
        super(LoginForm, self).__init__()
        self._login = None
        self._password = None
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        if "login" not in request or "password" not in request:
            raise TypeError("в запросе отсутствует логин или пароль")
        self.login_validator.is_valid(request["login"])
        self.password_validator.is_valid(request["password"])
        self._login = request["login"]
        self._password = request["password"]


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
# login, password = input().split()
login, password = "vbogoduhov Gfh11235813!".split()
try:
    lg.form({"login": login, "password": password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
