class Thing(object):
    """docstring for Thing."""

    def __init__(self, name, weight):
        super(Thing, self).__init__()
        self.name = name
        self.weight = weight
        self.current_weight = 0


class Bag(object):
    """docstring for Bag."""

    def __init__(self, max_weight):
        super(Bag, self).__init__()
        self.max_weight = max_weight
        self.things = []
        self.current_weight = 0

    def add_thing(self, thing):
        if self.current_weight + thing.weight <= self.max_weight:
            self.things.append(thing)
            self.current_weight += thing.weight
        else:
            raise ValueError("превышен суммарный вес предметов")

    def __check_index(self, key):
        if key < 0 or key > len(self.things):
            raise IndexError("неверный индекс")

    def __getitem__(self, key):
        self.__check_index(key)
        return self.things[key]

    def __setitem__(self, key, value):
        self.__check_index(key)
        tmp_thing = self.things[key]
        if self.current_weight - tmp_thing.weight + value.weight <= self.max_weight:
            self.things[key] = value
            self.current_weight = self.current_weight - tmp_thing.weight + value.weight
        else:
            raise ValueError("превышен суммарный вес предметов")

    def __delitem__(self, key):
        self.__check_index(key)
        tmp_thing = self.things[key]
        self.current_weight -= tmp_thing.weight
        self.things.pop(key)


# bag = Bag(1000)
# bag.add_thing(Thing("книга", 100))
# bag.add_thing(Thing("носки", 200))
# bag.add_thing(Thing("рубашка", 500))
# bag.add_thing(Thing("ножницы", 300))  # генерируется исключение ValueError
# print(bag[2].name)  # рубашка
# bag[1] = Thing("платок", 100)
# print(bag[1].name)  # платок
# del bag[0]
# print(bag[0].name)  # платок

b = Bag(700)
b.add_thing(Thing("книга", 100))
b.add_thing(Thing("носки", 200))

try:
    b.add_thing(Thing("рубашка", 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert (
    b[0].name == "книга" and b[0].weight == 100
), "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing("Python", 20)
b[1] = t
assert (
    b[1].name == "Python" and b[1].weight == 20
), "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == "Python" and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


b = Bag(700)
b.add_thing(Thing("книга", 100))
b.add_thing(Thing("носки", 200))

b[0] = Thing("рубашка", 500)

try:
    b[0] = Thing("рубашка", 800)
except ValueError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
