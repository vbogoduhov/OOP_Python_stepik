class Cell(object):
    """docstring for Cell."""

    def __init__(self, data):
        super(Cell, self).__init__()
        self.__data = data

    @property
    def data(self):
        """The data property."""
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __str__(self):
        return self.__data


class RowIterator(object):
    """docstring for RowIterator."""

    def __init__(self, row):
        super(RowIterator, self).__init__()
        self.row = row

    def __iter__(self):
        self.indx = -1
        return self

    def __next__(self):
        if self.indx < len(self.row) - 1:
            self.indx += 1
            return self.row[self.indx].data
        else:
            raise StopIteration


class TableValues(object):
    """docstring for TableValues."""

    def __init__(self, rows, cols, type_data=int):
        super(TableValues, self).__init__()
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def __check_index(self, key):
        r, c = key[0], key[1]
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            raise IndexError("неверный индекс")

    def __getitem__(self, key):
        self.__check_index(key)
        return self.table[key[0]][key[1]].data

    def __setitem__(self, key, value):
        self.__check_index(key)
        if not isinstance(value, self.type_data):
            raise TypeError("неверный тип присваиваемых данных")
        self.table[key[0]][key[1]].data = value

    def __iter__(self):
        self.row = -1
        return self

    def __next__(self):
        if self.row < self.rows - 1:
            self.row += 1
            return iter(RowIterator(self.table[self.row]))
        else:
            raise StopIteration


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert (
            type(value) == int and value == 0
        ), "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"


tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"


try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"


try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
