class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)
        
        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)

# здесь объявляйте класс Money
class Money(object):
    """docstring for Money."""
    def __init__(self, value):
        super(Money, self).__init__()
        self._money = value

    @property
    def money(self):
        """The money property."""
        return self._money
    @money.setter
    def money(self, value):
        self._money = value

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('сумма должна быть числом')
        object.__setattr__(self, key, value)


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"

m1 = MoneyR(1)
print(m1.money, m1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
m = m1 + m2  # TypeError
