import random


class RandomPassword:
    """Для генерации случайных паролей"""

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwds):
        password = random.sample(
            self.psw_chars, k=random.randint(self.min_length, self.max_length)
        )
        return "".join(password)

