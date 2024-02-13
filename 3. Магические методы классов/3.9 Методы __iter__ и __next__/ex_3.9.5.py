class Person(object):
    """docstring for Person."""

    def __init__(self, fio, job, old, salary, year_job):
        super(Person, self).__init__()
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.keys = ["fio", "job", "old", "salary", "year_job"]

    @classmethod
    def check_indx(cls, indx):
        if indx < 0 or indx > 4:
            raise IndexError("неверный индекс")
        else:
            return True

    def __getitem__(self, key):
        self.check_indx(key)
        return self.__dict__[self.keys[key]]

    def __setitem__(self, key, value):
        self.check_indx(key)
        self.__dict__[self.keys[key]] = value

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < 5:
            self.value += 1
            return self.__dict__[self.keys[self.value-1]]
        else:
            raise StopIteration


pers = Person("Гейтс Б.", "бизнесмен", 61, 1000000, 46)
pers[0] = "Балакирев С.М."
print(pers.__dict__)
for v in pers:
    print(v)
