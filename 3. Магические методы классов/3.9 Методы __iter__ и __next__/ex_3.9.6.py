class TriangleListIterator(object):
    """docstring for TriangleListIterator."""

    def __init__(self, lst):
        super(TriangleListIterator, self).__init__()
        self.lst = lst
        self.value = 0
        self.lst_rows = len(self.lst)

    def __iter__(self):
        self.value_row = 0
        self.value_col = -1
        return self

    def __next__(self):
        if self.value_row <= self.lst_rows - 1:
            if self.value_col < self.value_row:
                self.value_col += 1
                return self.lst[self.value_row][self.value_col]
            else:
                self.value_col = 0
                self.value_row += 1
                if self.value_row != self.lst_rows:
                    return self.lst[self.value_row][self.value_col]
                else:
                    raise StopIteration
        else:
            raise StopIteration


lst_int = [
    ["00", '01','02','03'],
    ["11", "12",'13','14'],
    ["21", "22"],
    ["31", "32", "33", "34"],
    ["41", "42", "43", "44", "45"],
]

it = TriangleListIterator(lst_int)

# for x in tr:
#     print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)
