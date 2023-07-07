import random as rnd
class Cell:
    """
    Класс для реализации клетки игрового поля
    """
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    """
    Класс для реализации игрового поля
    """
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = self.create_cells()
        self.init()
        self.set_around_mines()

    def init(self):
        for lst in self.pole:
            for cell in lst:
                tmp_mine = rnd.choice([True, False])
                if tmp_mine:
                    if self.M > 0:
                        cell.mine = tmp_mine
                        self.M -= 1

    def show(self):
        for lst in self.pole:
            for cell in lst:
                char = self.get_char(cell)
                print(char, end=' ')
            print('\n')

    def create_cells(self):
        return [[Cell() for _ in range(self.N)] for _ in range(self.N)]

    def get_char(self, cell):
        char = None
        if not cell.fl_open:
            char = '#'
        else:
            if cell.mine:
                char = '*'
            else:
                char = str(cell.around_mines)
        return char

    def rnd_open_cell(self):
        for lst in self.pole:
            for cell in lst:
                cell.fl_open = True

    def get_around_mines(self, row, col):
        count_mines = 0
        if not self.pole[row][col].mine:
            if row == 0:
                if col == 0:
                    lst_cells = self.pole[row][:col + 2] + self.pole[row + 1][:col + 2]
                    count_mines = self.get_mines_from_cells(lst_cells)
                if col == self.N-1:
                    lst_cells = self.pole[row][col-1:] + self.pole[row+1][col-1:]
                    count_mines = self.get_mines_from_cells(lst_cells)
                if col in range(1, self.N-1):
                    lst_cells = self.pole[row][col-1:col+2] + self.pole[row+1][col-1:col+2]
                    count_mines = self.get_mines_from_cells(lst_cells)
            if row == self.N-1:
                if col == 0:
                    lst_cells = self.pole[row-1][:col+2] + self.pole[row][:col+2]
                    count_mines = self.get_mines_from_cells(lst_cells)
                if col == self.N-1:
                    lst_cells = self.pole[row-1][col-1:] + self.pole[row][col-1:]
                    count_mines = self.get_mines_from_cells(lst_cells)
                if col in range(1, self.N-1):
                    lst_cells = self.pole[row-1][col-1:col+2] + self.pole[row][col-1:col+2]
                    count_mines = self.get_mines_from_cells(lst_cells)
            if row in range(1, self.N-1):
                if col in range(2):
                    lst_cells = self.pole[row-1][:col+2] + self.pole[row][:col+2] + self.pole[row+1][:col+2]
                    count_mines = self.get_mines_from_cells(lst_cells)
                if col in range(self.N-2, self.N):
                    lst_cells = self.pole[row-1][col-1:] + self.pole[row][col-1:] + self.pole[row+1][col-1:]
                    count_mines = self.get_mines_from_cells(lst_cells)
                if col in range(2, self.N-2):
                    lst_cells = self.pole[row-1][col-1:col+2] + self.pole[row][col-1:col+2] + self.pole[row+1][col-1:col+2]
                    count_mines = self.get_mines_from_cells(lst_cells)


        return count_mines

    def get_mines_from_cells(self, lst_cell):
        count_mines = 0
        for cell in lst_cell:
            count_mines += cell.mine

        return count_mines


    def set_around_mines(self):
        for r, lst in enumerate(self.pole):
            for c, cell in enumerate(lst):
                around_mines = self.get_around_mines(r, c)
                cell.around_mines = around_mines

pole_game = GamePole(10, 12)
pole_game.show()
print("==============================")
pole_game.rnd_open_cell()
pole_game.show()