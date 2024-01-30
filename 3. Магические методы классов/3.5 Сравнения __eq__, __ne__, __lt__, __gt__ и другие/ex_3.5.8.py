class CentralBank(object):
    """docstring for CenterBank."""

    rates = {"rub": 72.5, "dollar": 1.0, "euro": 1.15}

    def __new__(cls, *args, **kwargs):
        return

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money(object):
    """docstring for Money."""

    type_money = None

    def __init__(self, volume=0):
        super(Money, self).__init__()
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        """The cb property."""
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        """The volume property."""
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def get_volume(self, other):
        if other.cb is None:
            raise ValueError("Неизвестен курс валют.")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.get_volume(other)

        return abs(v1 - v2) < 0.1

    def __gt__(self, other):
        v1, v2 = self.get_volume(other)

        return v1 > v2

    def __ge__(self, other):
        v1, v2 = self.get_volume(other)

        return v1 >= v2


class MoneyR(Money):
    """docstring for MoneyR."""

    type_money = "rub"


class MoneyD(Money):
    """docstring for MoneyD."""

    type_money = "dollar"


class MoneyE(Money):
    """docstring for MoneyE."""

    type_money = "euro"


CentralBank.rates = {"rub": 72.5, "dollar": 1.0, "euro": 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("not bad")
else:
    print("go fast")
