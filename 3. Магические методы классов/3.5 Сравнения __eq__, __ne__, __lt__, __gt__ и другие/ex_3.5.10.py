class Thing(object):
    """docstring for Thing."""

    def __init__(self, name, mass):
        super(Thing, self).__init__()
        self.name = name
        self.mass = mass

    def __setattr__(self, key, value):
        if key == "name" and isinstance(value, str):
            object.__setattr__(self, key, value)
        if key == "mass" and isinstance(value, (int, float)):
            object.__setattr__(self, key, value)

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


class Box(object):
    """docstring for Box."""

    def __init__(self):
        super(Box, self).__init__()
        self.things = []

    def add_thing(self, obj):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, otherbox):
        ob = otherbox.get_things()
        if len(self.things) == len(ob):
            for th in self.things:
                if not th in ob:
                    return False
            return True
        else:
            return False


b1 = Box()
b2 = Box()

b1.add_thing(Thing("мел", 100))
b1.add_thing(Thing("тряпка", 200))
b1.add_thing(Thing("доска", 2000))

b2.add_thing(Thing("тряпка", 200))
b2.add_thing(Thing("мел", 100))
b2.add_thing(Thing("доска", 2000))

res = b1 == b2  # True
print(res)
