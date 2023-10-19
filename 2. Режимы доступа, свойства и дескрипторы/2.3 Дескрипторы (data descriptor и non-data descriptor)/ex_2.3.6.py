class FlaotValue:
    """
    Дескриптор
    """
    @classmethod
    def verify_value(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_value(value)
        instance.__dict__[self.name] = value

class Cell:
    """
    Ячейки
    """
    value = FlaotValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    """
    Таблица
    """
    def __init__(self, N, M):
        # count = 0
        self.cells = [[] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                # count += 1
                self.cells[i].append(Cell(0.0))

table = TableSheet(5, 3)
#print(table.cells[0][0].value)
count = 0
for i in range(5):
    for j in range(3):
        count += 1
        table.cells[i][j].value = float(count)

res = []
for i in range(5):
    for j in range(3):
        res.append(table.cells[i][j].value)
print(res)