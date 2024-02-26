class ItemAttrs(object):
    """docstring for ItemAttrs."""
    def __getitem__(self, key):
        keys = list(self.__dict__.keys())
        return getattr(self, keys[key])

    def __setitem__(self, key, value):
        keys = list(self.__dict__.keys())
        setattr(self, keys[key], value)

class Point(ItemAttrs):
    """docstring for Point."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
print(x, y, pt[0], pt[1])
