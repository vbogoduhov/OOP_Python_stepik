class Cell(object):
    """docstring for Cell."""

    def __init__(self, value):
        super(Cell, self).__init__()
        self.value = value


class SparseTable(object):
    """docstring for SparseTable."""

    def __init__(self):
        super(SparseTable, self).__init__()
        self.rows = 0
        self.cols = 0
        self.cells = {}

    def __get_value_row_col(self, coords, mode="rows"):
        res_value = 0
        if mode == "rows":
            lst_rows = [item[0] for item in coords]
            res_value = max(lst_rows)
        if mode == "cols":
            lst_cols = [item[1] for item in coords]
            res_value = max(lst_cols)
        return res_value

    def add_data(self, row, col, data):
        coord = (row, col)
        self.cells[coord] = data
        self.reindex()

    def remove_data(self, row, col):
        coord = (row, col)
        if coord not in self.cells:
            raise IndexError("ячейка с указанными индексами не существует")
        else:
            self.cells.pop(coord)
        self.reindex()

    def reindex(self):
        keys = self.cells.keys()
        self.rows = self.__get_value_row_col(keys, mode="rows") + 1
        self.cols = self.__get_value_row_col(keys, mode="cols") + 1

    def __getitem__(self, key):
        if key not in self.cells:
            raise ValueError("данные по указанным индексам отсутствуют")
        else:
            return self.cells[key].value

    def __setitem__(self, key, value):
        if key not in self.cells:
            self.add_data(key[0], key[1], Cell(value))
        else:
            self.cells[key].value = value


#
# st = SparseTable()
# st.add_data(2, 5, Cell("cell_25"))
# st.add_data(0, 0, Cell("cell_00"))
# st[2, 5] = 25  # изменение значения существующей ячейки
# st[11, 7] = "cell_117"  # создание новой ячейки
# print(st[0, 0])  # cell_00
# st.remove_data(2, 5)
# print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5]  # ValueError
st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert (
    st[3, 2] == 100
), "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st[4, 7] = 132
assert st.rows == 5 and st.cols == 8, "неверные значения атрибутов rows и cols"

st.remove_data(4, 7)
assert (
    st.rows == 4 and st.cols == 6
), "неверные значения атрибутов rows и cols, возможно, некорректно отработал метод remove_data"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell("5")
assert (
    d.value == "5"
), "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
st.remove_data(12, 3)  # IndexError
