class IterColumn(object):
    """docstring for IterColumn."""

    def __init__(self, lst, column=0):
        super(IterColumn, self).__init__()
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.value_row = -1
        return self

    def __next__(self):
        if self.value_row < len(self.lst) - 1:
            self.value_row += 1
            return self.lst[self.value_row][self.column]
        else:
            raise StopIteration


lst = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
    ["30", "31", "32", "33"],
    ["40", "41", "42", "43"],
]

it = IterColumn(lst, 1)
for (
    x
) in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
