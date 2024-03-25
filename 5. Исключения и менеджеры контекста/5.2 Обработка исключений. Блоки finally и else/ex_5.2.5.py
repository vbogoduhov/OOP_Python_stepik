class Point(object):
    """docstring for Point."""

    def __init__(self, x=0, y=0):
        super(Point, self).__init__()
        self._x = x
        self._y = y

    def __str__(self):
        return f"Point: x = {self._x}, y = {self._y}"


# in_text = input()
in_text = "abc 19"
lst_in = in_text.split()


def check_values(value):
    if value.isdigit():
        try:
            return int(value)
        except ValueError:
            return float(value)
    else:
        if value[0] != "-" and value.find(".") != -1:
            try:
                return float(value)
            except ValueError:
                pass
        if value[0] == "-" and value.find(".") == -1 and value[1:].isdigit():
            try:
                return int(value)
            except ValueError:
                return float(value)
    return value


p = None

try:
    val1, val2 = check_values(lst_in[0]), check_values(lst_in[1])
    if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
        p = Point(val1, val2)
    else:
        p = Point()
except:
    pass
finally:
    print(p)
