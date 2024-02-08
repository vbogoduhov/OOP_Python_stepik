class Number(object):
    """docstring for Number."""

    __type = None

    def __init__(self, start_value=None):
        super(Number, self).__init__()
        self.__value = start_value

    @property
    def value(self):
        """The value property."""
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Integer(Number):
    """docstring for Integer."""

    __type = int

    def __init__(self, start_value=0):
        super(Integer, self).__init__(start_value)

    def __setattr__(self, key, value):
        if not isinstance(value, self.__type):
            raise ValueError("должно быть целое число")
        else:
            object.__setattr__(self, key, value)


class Float(Number):
    """docstring for Float."""

    __type = float

    def __init__(self, start_value=0.0):
        super(Float, self).__init__(start_value)

    def __setattr__(self, key, value):
        if not isinstance(value, self.__type):
            raise ValueError("Must have a float")
        else:
            object.__setattr__(self, key, value)


class Array(object):
    """docstring for Array."""

    def __init__(self, max_length, cell):
        super(Array, self).__init__()
        self.arrray = [cell() for _ in range(max_length)]

    def __check_indx(self, indx):
        if 0 > indx >= len(self.arrray):
            raise IndexError("неверный индекс для доступа к элементам массива")
        else:
            return True

    def __getitem__(self, key):
        if self.__check_indx(key):
            return self.arrray[key].value

    def __setitem__(self, key, value):
        if self.__check_indx(key):
            self.arrray[key].value = value

    def __str__(self):
        lst = [str(item.value) for item in self.arrray]
        return " ".join(lst)


n = Integer()

n.value = 10
print(n.value)
f = Float()
print(f.value)
f.value = 12.354
print(f.value)

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)
