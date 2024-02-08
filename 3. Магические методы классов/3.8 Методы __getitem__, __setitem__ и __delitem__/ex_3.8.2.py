class Record(object):
    """docstring for Record."""

    def __init__(self, *args, **kwargs):
        super(Record, self).__init__()
        # self.__dict__.update(kwargs)
        # self.keys = list(self.__dict__.keys())
        self.keys = []
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)
            self.keys.append(k)

    def __getitem__(self, key):
        if key >= len(self.keys):
            raise IndexError("неверный индекс поля")
        else:
            return object.__getattribute__(self, self.keys[key])

    def __setitem__(self, key, value):
        if key >= len(self.keys):
            raise IndexError("неверный индекс поля")
        else:
            return object.__setattr__(self, self.keys[key], value)


r = Record(pk=1, title="Python OOP", author="Balakirev")

print(r.pk)  # 1
print(r.title)  # Python ООП
print(r.author)  # Балакирев

r[0] = 2  # доступ к полю pk
r[1] = "Super kurs on Python"  # доступ к полю title
r[2] = "Balakirev C.M."  # доступ к полю author
print(r[1])  # Супер курс по ООП
# r[3]  # генерируется исключение IndexError
print(r.pk)  # 1
print(r.title)  # Python ООП
print(r.author)  # Балакирев
