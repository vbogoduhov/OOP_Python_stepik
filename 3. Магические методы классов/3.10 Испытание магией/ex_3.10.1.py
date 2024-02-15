from random import randint


class Cell(object):
    """docstring for Cell."""

    def __init__(self):
        super(Cell, self).__init__()
        self.__value = 0

    @property
    def value(self):
        """The value property."""
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __bool__(self):
        return True if self.value == 0 else False


class TicTacToe(object):
    """docstring for TicTacToe."""

    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)
    CHAR = {0: " - ", 1: " X ", 2: " O "}

    def __init__(self):
        super(TicTacToe, self).__init__()
        self.pole = tuple([tuple([Cell() for _ in range(3)]) for _ in range(3)])
        self.__get_free_cells()
        self.__game_over = False
        self.__free_cells_end = False
        self.__lst_free_cells = []
        self.__flag_human_win = False
        self.__flag_computer_win = False

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL
        self.__get_free_cells()
        self.__game_over = False
        self.__free_cells_end = False
        self.__lst_free_cells = []
        self.__flag_human_win = False
        self.__flag_computer_win = False

    def __get_free_cells(self):
        self.__lst_free_cells = []
        for r, v in enumerate(self.pole):
            for c, cell in enumerate(v):
                if cell:
                    self.__lst_free_cells.append((r, c))
        if len(self.__lst_free_cells) == 0:
            self.__free_cells_end = True
            self.__game_over = True
        else:
            self.__free_cells_end = False

    def __check_index(self, indx):
        r, c = indx[0], indx[1]
        if (
            not isinstance(r, int)
            or not isinstance(c, int)
            or r < 0
            or r > 2
            or c < 0
            or c > 2
        ):
            raise IndexError("некорректно указанные индексы")

    def __getitem__(self, key):
        self.__check_index(key)
        return self.pole[key[0]][key[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        if not self.__game_over and self.pole[key[0]][key[1]]:
            self.pole[key[0]][key[1]].value = value
            self.__get_free_cells()
            self.__status_game()

    def show(self):
        for row in self.pole:
            for cell in row:
                char = self.__get_char(cell)
                print(char, end="")
            print()
        print()

    def human_go(self):
        coord = tuple(list(map(int, input("Введите координаты ячейки: ").split())))
        r, c = coord[0], coord[1]
        self[r, c] = self.HUMAN_X

    def computer_go(self):
        indx_free_cell = randint(0, len(self.__lst_free_cells) - 1)
        coord = self.__lst_free_cells[indx_free_cell]
        r, c = coord[0], coord[1]
        self[r, c] = self.COMPUTER_O

    @property
    def is_human_win(self):
        """The is_numan_win property."""
        return self.__flag_human_win

    @property
    def is_computer_win(self):
        """The is_computer_win property."""
        return self.__flag_computer_win

    @property
    def is_draw(self):
        """The is_draw property."""
        if (
            self.__game_over
            and self.__free_cells_end
            and not self.__flag_human_win
            and not self.__flag_computer_win
        ):
            return True
        else:
            return False

    def __bool__(self):
        if (
            not self.__free_cells_end
            and not self.is_human_win
            and not self.is_computer_win
        ):
            return True
        else:
            return False

    def __get_char(self, cell):
        cell_value = cell.value
        char = self.CHAR[cell_value]
        return char

    def __status_game(self):
        lst_human_cell = [
            [1 if cell.value == 1 else 0 for cell in row] for row in self.pole
        ]
        lst_computer_cell = [
            [1 if cell.value == 2 else 0 for cell in row] for row in self.pole
        ]
        self.__flag_human_win = self.__is_win(lst_human_cell)
        self.__flag_computer_win = self.__is_win(lst_computer_cell)

    def __is_win(self, lst_cells):
        for i in range(3):
            if (
                sum(lst_cells[i]) == 3
                or sum([lst_cells[0][i] + lst_cells[1][i] + lst_cells[2][i]]) == 3
                or sum([lst_cells[0][0] + lst_cells[1][1] + lst_cells[2][2]]) == 3
                or sum([lst_cells[0][2] + lst_cells[1][1] + lst_cells[2][0]]) == 3
            ):
                return True
        return False


cell = Cell()
assert (
    cell.value == 0
), "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert (
    bool(cell) == False
), "функция bool для объекта класса Cell вернула неверное значение"

assert (
    hasattr(TicTacToe, "show")
    and hasattr(TicTacToe, "human_go")
    and hasattr(TicTacToe, "computer_go")
), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert (
    game[0, 0] == 0 and game[2, 2] == 0
), "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert (
    game[1, 1] == TicTacToe.HUMAN_X
), "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert (
    game[0, 0] == TicTacToe.COMPUTER_O
), "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert (
    game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL
), "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert (
    game.is_human_win == False
    and game.is_computer_win == False
    and game.is_draw == False
), "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert (
    game.is_human_win and game.is_computer_win == False and game.is_draw == False
), "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert (
    game.is_human_win == False and game.is_computer_win and game.is_draw == False
), "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
