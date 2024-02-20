class Tuple(tuple):
    """docstring for Tuple."""

    def __add__(self, iter_obj):
        if len(iter_obj):
            if not isinstance(iter_obj, tuple):
                res = tuple(self) + tuple(iter_obj)
            else:
                res = tuple(self) + iter_obj
        return Tuple(res)


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)
