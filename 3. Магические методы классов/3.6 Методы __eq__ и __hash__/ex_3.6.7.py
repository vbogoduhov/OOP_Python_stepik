class DataBase(object):
    """docstring for DataBase."""

    def __init__(self, path):
        super(DataBase, self).__init__()
        self.path = path
        self.dict_db = {}

    def write(self, record):
        if record in self.dict_db:
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]

    def read(self, pk):
        for item in list(self.dict_db.values()):
            for rec in item:
                if pk == rec.pk:
                    return rec


class Record(object):
    """docstring for Record."""

    count = 0

    def __init__(self, fio, descr, old):
        super(Record, self).__init__()
        Record.count += 1
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.count

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return True if hash(self) == hash(other) else False

    def __str__(self):
        return f"{self.fio}: {self.descr}, {self.old}, pk = {self.pk}"


lst_in = [
    "Балакирев С.М.; программист; 33",
    "Кузнецов Н.И.; разведчик-нелегал; 35",
    "Суворов А.В.; полководец; 42",
    "Иванов И.И.; фигурант всех подобных списков; 26",
    "Балакирев С.М.; преподаватель; 33",
]
db = DataBase("C:\Mega\db.db")
for rec in lst_in:
    t = rec.split(sep=";")
    db.write(Record(t[0], t[1], int(t[2])))


print(db.read(3))
