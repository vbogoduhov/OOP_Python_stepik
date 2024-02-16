class Thing(object):
    """docstring for Thing."""

    __id = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        Thing.__id += 1
        cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        super(Thing, self).__init__()
        self.id = self.__id
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self):
        return (
            self.id,
            self.name,
            self.price,
            self.weight,
            self.dims,
            self.memory,
            self.frm,
        )


class Table(Thing):
    """docstring for Table."""

    def __init__(self, name, price, weight, dims):
        super(Table, self).__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    """docstring for ElBook."""

    def __init__(self, name, price, memory, frm):
        super(ElBook, self).__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, "pdf")
print(*table.get_data())
print(*book.get_data())
print(table.id, book.id)
