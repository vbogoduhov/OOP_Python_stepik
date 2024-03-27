class TupleLimit(tuple):
    """docstring for TupleLimit."""

    def __new__(cls, *args):
        if len(args[0]) > args[1]:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super(TupleLimit, cls).__new__(cls, tuple(args[0]))

    def __str__(self):
        return " ".join(map(str, self))

    def __repr__(self):
        return " ".join(map(str, self))

try:
    tl = TupleLimit([1, 3.2, 4, 5, 6.1, 7, 0], 10)
    print(tl)
except Exception as e:
    print(e)

