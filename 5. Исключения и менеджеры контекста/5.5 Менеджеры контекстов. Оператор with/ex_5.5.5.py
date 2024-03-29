from re import template


class Box(object):
    """docstring for Box."""

    def __init__(self, name, max_weight):
        super(Box, self).__init__()
        self._name = name
        self._max_weight = max_weight
        self._things = []
        self._cur_weight = 0

    def add_thing(self, obj):
        if self._cur_weight < self._max_weight:
            tmp_weight = self._cur_weight + obj[1]
            if tmp_weight > self._max_weight:
                raise ValueError("превышен суммарный вес вещей")
            else:
                self._things.append(obj)
                self._cur_weight += obj[1]


class BoxDefender(object):
    """docstring for BoxDefender."""

    def __init__(self, box):
        super(BoxDefender, self).__init__()
        self.box = box

    def __enter__(self):
        self.tmp_box = Box(self.box._name, self.box._max_weight)
        self.tmp_box._cur_weight = self.box._cur_weight
        self.tmp_box._things = self.box._things[:]
        return self.tmp_box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.box._things = self.tmp_box._things[:]
            self.box._cur_weight = self.tmp_box._cur_weight
        return False


b = Box("name", 2000)
assert (
    b._name == "name" and b._max_weight == 2000
), "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2

else:
    assert False, "не сгенерировалось исключение ValueError"


try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"
