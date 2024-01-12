class InputDigit(object):
    """Класс-декоратор"""

    def __init__(self, func):
        self.__fn_input = func

    def __call__(self):
        return [int(i) for i in self.__fn_input().split(sep=" ")]


@InputDigit
def input_dg():
    return input()


res = input_dg()

print(res)
