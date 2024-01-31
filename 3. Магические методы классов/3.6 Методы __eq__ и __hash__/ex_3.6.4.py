class Rect(object):
    """docstring for  Rect."""

    def __init__(self, x, y, width, height):
        super(Rect, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.width, self.height))

    def __len__(self, other):
        return True if hash(self) == hash(other) else False


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)  # h1 == h2

print(h1 == h2)
