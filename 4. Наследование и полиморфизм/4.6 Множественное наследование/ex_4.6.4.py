class Digit(object):
    """docstring for Digit."""
    def __init__(self, value):
        super(Digit, self).__init__()
        self._value = value

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        object.__setattr__(self, key, value)

class Integer(Digit):
    """docstring for Integer."""
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        super(Integer, self).__init__(value)


class Float(Digit):
    """docstring for Float."""
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        super(Float, self).__init__(value)


class Positive(Digit):
    """docstring for Positive."""
    def __init__(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super(Positive, self).__init__(value)


class Negative(Digit):
    """docstring for Negative."""
    def __init__(self, value):
        if value >=0:
            raise TypeError('значение не соответствует типу объекта')
        super(Negative, self).__init__(value)

class PrimeNumber(Integer, Positive):
    """docstring for PrimeNumber."""
    def __init__(self, value):
        super(PrimeNumber, self).__init__(value)

class FloatPositive(Float, Positive):
    """docstring for FloatPositive."""
    def __init__(self, value):
        super(FloatPositive, self).__init__(value)
    
digits = [
    PrimeNumber(5),
    PrimeNumber(0),
    PrimeNumber(11),
    FloatPositive(3.5),
    FloatPositive(11.2),
    FloatPositive(5.9),
    FloatPositive(8.6),
    FloatPositive(8.1)
]

lst_positive = [x for x in digits  if isinstance(x, Positive)]
lst_float = [x for x in digits if isinstance(x, Float)]
# for x in lst_positive:
#     print(x._value)
for x in lst_float:
    print(x._value)


