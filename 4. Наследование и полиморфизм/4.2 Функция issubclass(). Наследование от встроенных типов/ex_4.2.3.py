class ListInteger(list):
    """docstring for ListInteger."""

    def __init__(self, *args):
        for i in args[0]:
            if not isinstance(i, int):
                raise TypeError("можно передавать только целочисленные значения")
        super(ListInteger, self).__init__(*args)

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("можно передавать только целочисленные значения")
        super().__setitem__(key, value)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("можно передавать только целочисленные значения")
        super().append(value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5  # TypeError
l = ListInteger((1, 5, 10.5, 9.3))
print(l)
