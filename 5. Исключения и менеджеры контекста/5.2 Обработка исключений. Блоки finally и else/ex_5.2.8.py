class Rect(object):
    """docstring for Rect."""

    def __init__(self, x, y, width, height):
        super(Rect, self).__init__()
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.__top = ((self._x, self._y), (self._x + self._width, self._y))
        self.__botom = (
            (self._x, self._y + self._height),
            (self._x + self._width, self._y + self._height),
        )
        self.__left = ((self._x, self._y), (self._x, self._y + self._height))
        self.__right = (
            (self._x + self._width, self._y),
            (self._x + self._width, self._y + self._height),
        )

    def __setattr__(self, key, value):
        if key in ("_x", "_y"):
            if not isinstance(value, (int, float)):
                raise ValueError("некорректные координаты и параметры прямоугольника")
        if key in ("_width", "_height"):
            if value <= 0:
                raise ValueError("некорректные координаты и параметры прямоугольника")
        object.__setattr__(self, key, value)

    def __eq__(self, rect):
        if (
            self._x == rect._x
            and self._y == rect._y
            and self._width == rect._width
            and self._height == rect._height
        ):
            return True
        return False

    def is_collision(self, rect):
        if not (
            self.top[0][1] > rect.botom[1][1]
            or self.botom[1][1] < rect.top[0][1]
            or self.left[0][0] > rect.right[1][0]
            or self.right[1][0] < rect.left[0][0]
        ):
            raise TypeError("прямоугольники пересекаются")

    @property
    def top(self):
        """The top property."""
        return self.__top

    @top.setter
    def top(self, value):
        self.__top = value

    @property
    def botom(self):
        """The botom property."""
        return self.__botom

    @botom.setter
    def botom(self, value):
        self.__botom = value

    @property
    def left(self):
        """The left property."""
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        """The rigth property."""
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []
for rect in lst_rect:
    try:
        for other in lst_rect:
            if other != rect:
                rect.is_collision(other)
    except TypeError:
        pass
    else:
        lst_not_collision.append(rect)


r = Rect(1, 2, 10, 20)
assert (
    r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20
), "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert (
    len(lst_not_collision) == 1
), "неверное число элементов в списке lst_not_collision"


def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True


f = list(filter(not_collision, lst_rect))
assert (
    lst_not_collision == f
), "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
