class Vector(object):
    """docstring for Vector."""

    def __init__(self, *args):
        super(Vector, self).__init__()
        self.coords = args
        self.razm = len(self.coords)

    def get_coords(self):
        return self.coords

    def __add__(self, other):
        self.__check_razm(other)
        out_coord = [v + other.coords[i] for i, v in enumerate(self.coords)]
        if isinstance(other, VectorInt):
            return VectorInt(*out_coord)
        return Vector(*out_coord)

    def __sub__(self, other):
        self.__check_razm(other)
        out_coord = [v - other.coords[i] for i, v in enumerate(self.coords)]
        if isinstance(other, VectorInt):
            return VectorInt(*out_coord)
        return Vector(*out_coord)

    def __check_razm(self, other):
        if self.razm != other.razm:
            raise TypeError("размерности векторов не совпадают")
        return True


class VectorInt(Vector):
    """docstring for VectorInt."""

    def __setattr__(self, key, value):
        if key == "coords":
            for i in value:
                if not isinstance(i, int):
                    raise ValueError("координаты должны быть целыми числами")
        object.__setattr__(self, key, value)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (
    4,
    6,
    8,
), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
    -2,
    -2,
    -2,
), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"


v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert (
    type(v) == VectorInt
), "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert (
    type(v) == Vector
), "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
