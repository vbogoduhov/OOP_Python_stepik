# здесь объявляйте классы CellException, CellIntegerException, CellFloatException, CellStringException
class CellException(Exception):
    """docstring for CellException."""


class CellIntegerException(CellException):
    """docstring for CellIntegerException."""


class CellFloatException(CellException):
    """docstring for CellFloatException."""


class CellStringException(CellException):
    """docstring for CellStringException."""


# здесь объявляйте классы CellInteger, CellFloat, CellString
class CellInteger(object):
    """docstring for CellInteger."""

    def __init__(self, min_value, max_value):
        super(CellInteger, self).__init__()
        self.__value = None
        self._min_value = min_value
        self._max_value = max_value

    @property
    def value(self):
        """The value property."""
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if key == "_CellInteger__value":
            if value is not None and (
                value < self._min_value or value > self._max_value
            ):
                raise CellIntegerException("значение выходит за допустимый диапазон")
        object.__setattr__(self, key, value)


class CellFloat(object):
    """docstring for CellFloat."""

    def __init__(self, min_value, max_value):
        super(CellFloat, self).__init__()
        self.__value = None
        self._min_value = min_value
        self._max_value = max_value

    @property
    def value(self):
        """The value property."""
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if key == "_CellFloat__value":
            if value is not None and (
                value < self._min_value or value > self._max_value
            ):
                raise CellFloatException("значение выходит за допустимый диапазон")
        object.__setattr__(self, key, value)


class CellString(object):
    """docstring for CellString."""

    def __init__(self, min_length, max_length):
        super(CellString, self).__init__()
        self.__value = None
        self._min_length = min_length
        self._max_length = max_length

    @property
    def value(self):
        """The value property."""
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if key == "_CellString__value":
            if value is not None and (
                len(value) < self._min_length or len(value) > self._max_length
            ):
                raise CellStringException("длина строки выходит за допустимый диапазон")
        object.__setattr__(self, key, value)


# здесь объявляйте класс TupleData
class TupleData(object):
    """docstring for TupleData."""

    __types = (CellInteger, CellFloat, CellString)

    def __init__(self, *args):
        super(TupleData, self).__init__()
        self._lst_data = [cell for cell in args if isinstance(cell, self.__types)]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0 or key > (len(self._lst_data) - 1):
            raise IndexError
        self._lst_data[key].value = value

    def __getitem__(self, key):
        if not isinstance(key, int) or key < 0 or key > (len(self._lst_data) - 1):
            raise IndexError
        return self._lst_data[key].value

    def __iter__(self):
        self.ind = 0
        return self

    def __next__(self):
        if self.ind < len(self._lst_data):
            self.ind += 1
            return self[self.ind - 1]
        else:
            raise StopIteration

    def __len__(self):
        return len(self._lst_data)


# эти строчки в программе не менять!
ld = TupleData(
    CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100)
)

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")

t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, "sergey")
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"


cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"


cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"


cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert (
    issubclass(CellIntegerException, CellException)
    and issubclass(CellFloatException, CellException)
    and issubclass(CellStringException, CellException)
), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
