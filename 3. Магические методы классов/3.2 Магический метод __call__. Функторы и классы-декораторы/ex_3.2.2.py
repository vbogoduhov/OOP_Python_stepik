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


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for i in range(0, 3)]
print(*lst_pswd, sep="\n")
