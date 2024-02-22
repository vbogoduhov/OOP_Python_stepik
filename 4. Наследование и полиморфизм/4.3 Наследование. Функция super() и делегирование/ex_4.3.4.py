class Thing(object):
    """docstring for Thing."""

    def __init__(self, name, weight):
        super(Thing, self).__init__()
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    """docstring for ArtObject."""

    def __init__(self, name, weight, author, date):
        super(ArtObject, self).__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    """docstring for Computer."""

    def __init__(self, name, weight, memory, cpu):
        super(Computer, self).__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    """docstring for Auto."""

    def __init__(self, name, weight, dims):
        super(Auto, self).__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    """docstring for Mercedes."""

    def __init__(self, name, weight, dims, model, old):
        super(Mercedes, self).__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    """docstring for Toyota."""

    def __init__(self, name, weight, dims, model, wheel):
        super(Toyota, self).__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel
