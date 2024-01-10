class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get("login", "")
        self.password = request.get("password", "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        valid_string = args[0]
        return (
            True if self.min_length <= len(valid_string) <= self.max_length else False
        )


class CharsValidator:
    """Проверка на допустимые символы"""

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        str_for_valid = args[0]
        return True if len(set(str_for_valid) - set(self.chars)) == 0 else False
