from math import sqrt


class Line(object):
    """docstring for Line."""

    def __init__(self, x1, y1, x2, y2):
        super(Line, self).__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        l = sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        return 0 if l < 1 else 1
