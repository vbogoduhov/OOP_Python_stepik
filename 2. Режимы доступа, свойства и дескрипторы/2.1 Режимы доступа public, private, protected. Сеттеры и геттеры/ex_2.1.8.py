class Point:
    def __init__(self, x, y):
        if self.__check_coords(x, y):
            self.__x = x
            self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)

    def __check_coords(self, x, y):
        return type(x) in (int, float) and type(y) in (int, float)

class Rectangle:
    def __init__(self, *args):
        if len(args) == 2 and type(args[0]) is Point and type(args[1]) is Point:
            self.__sp = args[0]
            self.__ep = args[1]
        elif len(args) > 2:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


rect = Rectangle(0, 0, 20, 34)
rect.draw()
rect2 = Rectangle(Point(0, 0), Point(20, 34))
rect2.draw()