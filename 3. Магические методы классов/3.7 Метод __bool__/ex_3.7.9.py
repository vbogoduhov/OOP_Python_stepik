class Vector(object):
    """docstring for Vector."""

    def __init__(self, *args):
        super(Vector, self).__init__()
        self.__coords = args
        self.__razm = len(self.__coords)

    @property
    def razm(self):
        """The razm property."""
        return self.__razm

    @razm.setter
    def razm(self, value):
        self.__razm = value

    @property
    def coords(self):
        """The coords property."""
        return self.__coords

    @coords.setter
    def coords(self, value):
        self.__coords = value

    def __check_razm(self, other):
        if isinstance(other, Vector):
            return True if self.razm == other.razm else False

    def __add__(self, other):
        if isinstance(other, Vector):
            if not self.__check_razm(other):
                raise ArithmeticError("размерности векторов не совпадают")
            coord = [self.coords[i] + other.coords[i] for i in range(len(self.coords))]
        else:
            coord = [self.coords[i] + other for i in range(len(self.coords))]
        return Vector(*coord)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if not self.__check_razm(other):
                raise ArithmeticError("размерности векторов не совпадают")
            coord = [self.coords[i] * other.coords[i] for i in range(len(self.coords))]
        else:
            coord = [self.coords[i] * other for i in range(len(self.coords))]
        return Vector(*coord)

    def __sub__(self, other):
        if isinstance(other, Vector):
            if not self.__check_razm(other):
                raise ArithmeticError("размерности векторов не совпадают")
            coord = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
        else:
            coord = [self.coords[i] - other for i in range(len(self.coords))]
        return Vector(*coord)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            # for i, v in enumerate(self.coords):
            #     v += other.coords[i]
            self.coords = [
                self.coords[i] + other.coords[i] for i in range(len(self.coords))
            ]
        else:
            # for i, v in enumerate(self.coords):
            #     v += other
            self.coords = [self.coords[i] + other for i in range(len(self.coords))]

        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.coords = [
                self.coords[i] - other.coords[i] for i in range(len(self.coords))
            ]
            # for i, v in enumerate(self.coords):
            #     v -= other.coords[i]
        else:
            self.coords = [self.coords[i] - other for i in range(len(self.coords))]
            # for i, v in enumerate(self.coords):
            #     v -= other

        return self

    def __eq__(self, other):
        for i, v in enumerate(self.coords):
            if v != other.coords[i]:
                return False
        return True

    def __ne__(self, other):
        for i, v in enumerate(self.coords):
            if v != other.coords[i]:
                return True
        return False


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True
