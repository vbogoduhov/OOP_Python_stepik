class Cell(object):
    """docstring for Cell."""

    def __init__(self, value=0):
        super(Cell, self).__init__()
        self.value = value
        self.is_free = True

    def __bool__(self):
        return self.is_free


class TicTacToe(object):
    """docstring for TicTacToe."""

    def __init__(self):
        super(TicTacToe, self).__init__()
        self.pole = tuple([tuple([Cell() for _ in range(3)]) for _ in range(3)])

    def __check_index(self, indx):
        if (
            isinstance(indx, tuple)
            and isinstance(indx[0], int)
            and isinstance(indx[1], int)
        ):
            r, c = indx[0], indx[1]
            if r < 0 or r > 2 or c < 0 or c > 2:
                raise IndexError("неверный индекс клетки")
            else:
                return True
        return True

    def __check_cell(self, cell):
        if not cell:
            raise ValueError("клетка уже занята")
        else:
            return True

    def get_coords(self, coords):
        out_coords = []
        for coord in coords:
            if isinstance(coord, int):
                out_coords.append(coord)
            if isinstance(coord, slice):
                ind = coord.indices(3)
                out_coords.append(ind)
        return tuple(out_coords)

    def __getitem__(self, key):
        if self.__check_index(key):
            coord = self.get_coords(key)
            r = coord[0]
            c = coord[1]
            if isinstance(r, int) and isinstance(c, int):
                return self.pole[r][c].value
            else:
                out_res = []
                if isinstance(r, tuple):
                    for row in range(r[0], r[1], r[2]):
                        out_res.append(self.pole[row][c].value)

                if isinstance(c, tuple):
                    for col in range(c[0], c[1], c[2]):
                        out_res.append(self.pole[r][col].value)

            return tuple(out_res)

    def __setitem__(self, key, value):
        if self.__check_index(key):
            if self.__check_cell(self.pole[key[0]][key[1]]):
                self.pole[key[0]][key[1]].value = value

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_free = True


# game = TicTacToe()
# game.clear()
# game[0, 0] = 1
# game[1, 0] = 2
# # формируется поле:
# # 1 0 0
# # 2 0 0
# # 0 0 0
# # game[3, 2] = 2  # генерируется исключение IndexError
# if game[0, 0] == 0:
#     game[0, 0] = 2
# v1 = game[0, :]  # 1, 0, 0
# v2 = game[:, 0]  # 1, 2, 0
g = TicTacToe()
g.clear()
assert (
    g[0, 0] == 0 and g[2, 2] == 0
), "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert (
    g[1, 1] == 1 and g[2, 1] == 2
), "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"


try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert (
    g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3)
), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert (
    cell.value == 0
), "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
