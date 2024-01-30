class Body(object):
    """docstring for Body."""

    def __init__(self, name, ro, volume):
        super(Body, self).__init__()
        self.name = name
        self.ro = ro
        self.volume = volume

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.ro * self.volume == other.ro * other.volume
        else:
            return self.ro * self.volume == other

    def __gt__(self, other):
        if isinstance(other, Body):
            return self.ro * self.volume > other.ro * other.volume
        else:
            return self.ro * self.volume > other

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.ro * self.volume < other.ro * other.volume
        else:
            return self.ro * self.volume < other


b1 = Body("1", 10, 20)
b2 = Body("2", 10, 30)
b3 = Body("3", 1, 200)

print(b1 > b2)
print(b1 == b2)
print(b1 < 500)
print(b3 == 200)
