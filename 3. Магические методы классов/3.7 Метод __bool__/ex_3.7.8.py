from random import randint, choice
from re import escape


class Cell(object):
    """docstring for Cell."""

    def __init__(self):
        super(Cell, self).__init__()
        self.__number = 0
        self.__is_mine = False
        self.__is_open = False

    @property
    def number(self):
        """The number property."""
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def is_mine(self):
        """The is_mine property."""
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        self.__is_mine = value

    @property
    def is_open(self):
        """The is_open property."""
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        self.__is_open = value

    def __setattr__(self, key, value):
        if key in ("_Cell__is_mine", "_Cell__is_open"):
            if isinstance(value, bool):
                object.__setattr__(self, key, value)
            else:
                raise ValueError("недопустимое значение атрибута")
        else:
            if isinstance(value, int) and value in range(9):
                object.__setattr__(self, key, value)
            else:
                raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not self.is_open

    def __add__(self, other):
        if isinstance(other, Cell):
            return self.is_mine + other.is_mine
        if isinstance(other, int):
            return self.is_mine + other

    def __radd__(self, other):
        if isinstance(other, Cell):
            return other.is_mine + self.is_mine
        if isinstance(other, int):
            return other + self.is_mine


class GamePole(object):
    """docstring for GamePole."""

    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__count == 0:
            cls.__count += 1
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, N, M, total_mines):
        super(GamePole, self).__init__()
        self.row = N
        self.col = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.col)] for _ in range(self.row)]

    @property
    def pole(self):
        """The pole property."""
        return self.__pole_cells

    def init_pole(self):
        """Инициализация игрового поля, расстановка мин
        и количества мин вокруг клеток, в которых нет мин"""
        # count = 0
        for row in self.pole:
            for cell in row:
                if self.total_mines > 0:
                    mine = choice([True, False])
                    cell.is_mine = mine
                    if mine:
                        self.total_mines -= 1
        self.__set_arround_mines()

    def open_cell(self, i, j):
        """Открыть ячейку с коордианатами: i, j"""
        if (i < 0 or i > self.row - 1) or (j < 0 or j > self.col - 1):
            raise IndexError("некорректные индексы i, j клетки игрового поля")
        else:
            self.pole[i][j].is_open = True

    def show_pole(self):
        """Отобразить игровое поле в консоли"""
        pole = self.pole
        for row in pole:
            for cell in row:
                char = self.__get_char(cell)
                print(char, end=" ")
            print("\n")

    def __get_char(self, cell):
        """Возвращаем символ для отображения конкретной ячейки"""
        char = None
        if cell:
            char = "#"
        else:
            if cell.is_mine:
                char = "*"
            else:
                char = cell.number
        return char

    def __set_arround_mines(self):
        count = 0
        tmp_pole = [
            [0 for _ in range(len(self.pole) + 2)],
            *[[0] + row + [0] for row in self.pole],
            [0 for _ in range(len(self.pole) + 2)],
        ]
        for r in range(len(self.pole)):
            for c in range(len(self.pole[r])):
                if not self.pole[r][c].is_mine:
                    count_mine = sum(
                        tmp_pole[r][c : c + 3]
                        + tmp_pole[r + 1][c : c + 3]
                        + tmp_pole[r + 2][c : c + 3]
                    )
                    self.pole[r][c].number = count_mine


gp = GamePole(8, 8, 10)
gp.init_pole()
# gp.open_cell(1, 3)
# gp.open_cell(2, 5)
# gp.open_cell(3, 3)
for r in range(8):
    for c in range(8):
        gp.open_cell(r, c)
gp.show_pole()
