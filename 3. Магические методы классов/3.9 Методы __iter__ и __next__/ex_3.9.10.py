class Matrix(object):
    """docstring for Matrix."""

    def __init__(self, *args):
        super(Matrix, self).__init__()
        if len(args) == 3:
            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = args[2]
            self.lst_matrix = [
                [self.fill_value for _ in range(self.cols)] for _ in range(self.rows)
            ]
        if len(args) == 1:
            self.lst_matrix = args[0]
            self.rows = len(self.lst_matrix)
            self.cols = len(self.lst_matrix[0])

    def __setattr__(self, key, value):
        if (key == "rows" or key == "cols") and (not isinstance(value, int)):
            raise TypeError(
                "аргументы rows, cols - целые числа; fill_value - произвольное число"
            )
        if (key == "fill_value") and (not isinstance(value, (int, float))):
            raise TypeError(
                "аргументы rows, cols - целые числа; fill_value - произвольное число"
            )
        if key == "lst_matrix" and isinstance(value, list):
            self.__check_list(value)
        object.__setattr__(self, key, value)

    def __check_list(self, lst):
        if isinstance(lst, list):
            lenght = len(lst[0])
            for row in lst:
                if len(row) != lenght:
                    raise TypeError(
                        "список должен быть прямоугольным, состоящим из чисел"
                    )
                for i in row:
                    if not isinstance(i, (int, float)):
                        raise TypeError(
                            "список должен быть прямоугольным, состоящим из чисел"
                        )

    def __check_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("значения матрицы должны быть числами")
        return True

    def __check_index(self, indx):
        r, c = indx[0], indx[1]
        if not isinstance(r, int) or not isinstance(c, int):
            raise IndexError("недопустимые значения индексов")
        if (
            r < 0
            or r >= self.rows
            or c < 0
            or c >= self.cols
            or not isinstance(c, int)
            or not isinstance(r, int)
        ):
            raise IndexError("недопустимые значения индексов")
        return True

    def __getitem__(self, key):
        if self.__check_index(key):
            return self.lst_matrix[key[0]][key[1]]

    def __setitem__(self, key, value):
        if self.__check_index(key) and self.__check_value(value):
            self.lst_matrix[key[0]][key[1]] = value

    def __check_razm(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            return True
        else:
            raise ValueError("операции возможны только с матрицами равных размеров")

    def __add__(self, other):
        if isinstance(other, Matrix) and self.__check_razm(other):
            out_lst = [
                [val + other[r, c] for c, val in enumerate(row)]
                for r, row in enumerate(self.lst_matrix)
            ]
        if isinstance(other, int):
            out_lst = [[val + other for val in row] for row in self.lst_matrix]
        return Matrix(out_lst)

    def __sub__(self, other):
        if isinstance(other, Matrix) and self.__check_razm(other):
            out_lst = [
                [val - other[r, c] for c, val in enumerate(row)]
                for r, row in enumerate(self.lst_matrix)
            ]
        if isinstance(other, int):
            out_lst = [[val - other for val in row] for row in self.lst_matrix]
        return Matrix(out_lst)


list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix("1", 2, 0)
except TypeError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix["0", 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = "a"
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(
    matrix, Matrix
), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert (
    m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 and m2[0, 0] == 1
), "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert (
    id_m1_old != id_m1_new
), "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert (
    matrix[0, 0] == matrix[1, 1] == 0
), "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert (
    m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 and m2[0, 1] == 1
), "исходные матрицы не должны меняться при операции вычитания"
assert (
    identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1
), "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert (
    matrix[0, 0] == matrix[1, 1] == 1
), "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
