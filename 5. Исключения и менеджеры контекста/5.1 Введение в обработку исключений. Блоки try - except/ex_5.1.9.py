class Triangle(object):
    """docstring for Triangle."""

    def __init__(self, *args):
        super(Triangle, self).__init__()
        self.check_sides(args)
        self._a = args[0]
        self._b = args[1]
        self._c = args[2]

    @classmethod
    def check_sides(cls, args):
        if len(args) > 3:
            raise ValueError("из указанных длин сторон нельзя составить треугольник")
        a, b, c = args[0], args[1], args[2]
        if not (
            isinstance(a, (int, float))
            and a > 0
            and isinstance(b, (int, float))
            and b > 0
            and isinstance(c, (int, float))
            and c > 0
        ):
            raise TypeError("стороны треугольника должны быть положительными числами")

        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("из указанных длин сторон нельзя составить треугольник")


input_data = [
    (1.0, 4.54, 3),
    ("abc", 1, 2, 3),
    (-3, 3, 5.2),
    (4.2, 5.7, 8.7),
    (True, 3, 5),
    (7, 4, 6),
    (-1, 4.54, 3),
]

lst_tr = []

for item in input_data:
    try:
        tr = Triangle(*item)
        lst_tr.append(tr)
    except ValueError:
        pass
    except TypeError:
        pass
for tr in lst_tr:
    print(tr._a, tr._b, tr._c)
