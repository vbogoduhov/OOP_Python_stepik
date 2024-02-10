class IntegerValue(object):
    """Data descriptor"""
    @classmethod
    def verify_value(cls, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        else:
            return True

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.verify_value(value):
            instance.__dict__[self.name]=value

class CellInteger(object):
    """Object cell"""
    value = IntegerValue()
    def __init__(self, value=0):
        super(CellInteger, self).__init__()
        self.value = value

class TableValues(object):
    """docstring for TableValues."""
    def __init__(self, rows, cols, cell=None):
        super(TableValues, self).__init__()
        self.rows = rows
        self.cols = cols
        if cell is None:
            raise ValueError('параметр cell не указан')
        else:
            self.cells = tuple(tuple(cell() for _ in range(self.cols)) for _ in range(self.rows))

    def __getitem__(self, key):
        return self.cells[key[0]][key[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value

table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
