class IteratorAttrs(object):
    """docstring for IteratorAttrs."""

    def __init__(self):
        super(IteratorAttrs, self).__init__()

    def __iter__(self):
        return ((key, value) for key, value in self.__dict__.items())


class SmartPhone(IteratorAttrs):
    """docstring for SmartPhones."""

    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone("nokia", (15, 65), 65)
for key, value in phone:
    print(key, value)
