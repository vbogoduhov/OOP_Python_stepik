class Thing(object):
    """docstring for Thing."""

    def __init__(self, name, price, weight):
        super(Thing, self).__init__()
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    """docstring for DictShop."""

    def __init__(self, things={}):
        if not isinstance(things, dict):
            raise TypeError("аргумент должен быть словарем")
        else:
            for key in list(things.keys()):
                if not isinstance(key, Thing):
                    raise TypeError("ключами могут быть только объекты класса Thing")
            super().__init__(things)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError("ключами могут быть только объекты класса Thing")
        super().__setitem__(key, value)


th_1 = Thing("Ligy", 11000, 1978.55)
th_2 = Thing("Book", 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

dict_things[1] = th_1  # исключение TypeError
