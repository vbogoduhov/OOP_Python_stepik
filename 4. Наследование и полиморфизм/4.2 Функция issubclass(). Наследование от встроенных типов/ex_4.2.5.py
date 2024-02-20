class Protists(object):
    pass


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Person(Human):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Flower(Flowering):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Worm(Worms):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


lst_objs = [
    Monkey("мартышка", 30.4, 7),
    Monkey("шимпанзе", 24.6, 8),
    Person("Балакирев", 88, 34),
    Person("Верховный жрец", 67.5, 45),
    Flower("Тюльпан", 0.2, 1),
    Flower("Роза", 0.1, 2),
    Worm("червь", 0.01, 1),
    Worm("червь 2", 0.02, 1),
]

lst_animals = [obj for obj in lst_objs if isinstance(obj, Animals)]
lst_plants = [obj for obj in lst_objs if isinstance(obj, Plants)]
lst_mammals = [obj for obj in lst_objs if isinstance(obj, Mammals)]
