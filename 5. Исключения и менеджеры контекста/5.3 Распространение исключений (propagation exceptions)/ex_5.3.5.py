class Test(object):
    """docstring for Test."""

    __min_length = 10
    __max_length = 10000

    def __init__(self, descr):
        super(Test, self).__init__()
        if self.__min_length <= len(descr) <= self.__max_length:
            self._descr = descr
        else:
            raise ValueError("формулировка теста должна быть от 10 до 10 000 символов")

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    """docstring for TestAnsDigit."""

    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super(TestAnsDigit, self).__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, key, value):
        if key in ("ans_digit", "max_error_digit"):
            if not isinstance(value, (int, float)):
                raise ValueError("недопустимые значения аргументов теста")
        if key == "max_error_digit" and value < 0:
            raise ValueError("недопустимые значения аргументов теста")
        object.__setattr__(self, key, value)

    def run(self):
        ans = float(input())  # именно такой командой, ее прописывайте в методе run()
        return (
            True
            if (
                self.ans_digit - self.max_error_digit
                <= ans
                <= self.ans_digit + self.max_error_digit
            )
            else False
        )


# descr, ans = map(
#     str.strip, input().split("|")
# )  # например: Какое значение получится при вычислении 2+2? | 4
# ans = float(
#     ans
# )  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
# res = None
# try:
#     ts = TestAnsDigit(descr, ans)
#     res = ts.run()
# except Exception as e:
#     print(e)
# else:
#     print(res)


try:
    test = Test("descr")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"


try:
    test = Test("descr ghgfhgjg ghjghjg")
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)
try:
    t = TestAnsDigit("ffhgfh", 1)
except ValueError:
    assert  True
else:
    assert False

t = TestAnsDigit("ffhgfh fghfghfghfggfhfghfh", 1, 0.5)

try:
    t = TestAnsDigit("ffhgfh fghfghfghfggfhfghfh", 1, -0.5)
except ValueError:
    assert True
else:
    assert False
