class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

pt = Point(5, 8)
pt_clone = pt.clone()

print(pt.__dict__, pt_clone.__dict__)
