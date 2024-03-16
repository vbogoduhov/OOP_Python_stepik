class Star(object):
    """docstring for Star."""
    __slots__ = ('_name', '_massa', '_temp')
    def __init__(self, name, massa, temp):
        super(Star, self).__init__()
        self._name = name
        self._massa = massa
        self._temp = temp

class WhiteDwarf(Star):
    """docstring for WhiteDwarf."""
    __slots__ = '_type_star', '_radius',

    def __init__(self, name, massa, temp, type_star, radius):
        super(WhiteDwarf, self).__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius

class YellowDwarf(Star):
    """docstring for YellowDwarf."""
    __slots__ = '_type_star','_radius',

    def __init__(self, name, massa,temp, type_star, radius):
        super(YellowDwarf, self).__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius

class RedGiant(Star):
    """docstring for RedGiant."""
    __slots__ = '_type_star','_radius',
    def __init__(self, name, massa, temp,type_star, radius):
        super(RedGiant, self).__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius

class Pulsar(Star):
    """docstring for Pulsar."""
    __slots__ = '_type_star','_radius',

    def __init__(self, name, massa, temp,type_star, radius):
        super(Pulsar, self).__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius

stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
         WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
         WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
         YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]

white_dwarfs = [value for value in stars if isinstance(value, WhiteDwarf)]
for val in white_dwarfs:
    print(val._type_star)
