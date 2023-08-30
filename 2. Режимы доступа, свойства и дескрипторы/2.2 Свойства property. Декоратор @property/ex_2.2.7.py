class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x if self.__check_coord(x) else 0
        self.__y = y if self.__check_coord(y) else 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check_coord(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check_coord(y):
            self.__y = y

    def __check_coord(self, coord):
        if type(coord) in (int, float):
            return RadiusVector2D.MIN_COORD <= coord < RadiusVector2D.MAX_COORD
        else:
            return False

    @staticmethod
    def norm2(vector):
        return (vector.x**2 + vector.y**2)