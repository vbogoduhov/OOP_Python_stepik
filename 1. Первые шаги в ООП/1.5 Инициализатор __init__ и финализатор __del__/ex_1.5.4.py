import random as rd
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements = [rd.choice([Line, Rect, Ellipse])(rd.randint(0, i), rd.randint(0, i), rd.randint(0, i), rd.randint(0, 7)) for i in range(1,218)]

for line in elements:
    if isinstance(line, Line):
        line.sp = (0, 0)
        line.ep = (0, 0)


