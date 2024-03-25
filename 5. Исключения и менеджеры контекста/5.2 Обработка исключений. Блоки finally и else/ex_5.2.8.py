class Rect(object):
    """docstring for Rect."""

    def __init__(self, x, y, width, height):
        super(Rect, self).__init__()
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if key in ("_x", "_y"):
            if not isinstance(value, (int, float)):
                raise ValueError("некорректные координаты и параметры прямоугольника")
        if key in ("_width", "_height"):
            if value < 0:
                raise ValueError("некорректные координаты и параметры прямоугольника")
        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        pass
