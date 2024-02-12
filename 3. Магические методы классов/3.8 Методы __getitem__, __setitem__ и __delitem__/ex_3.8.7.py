class RadiusVector(object):
    """docstring for RadiusVector."""

    def __init__(self, *args):
        super(RadiusVector, self).__init__()
        self.coords = list(args)

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.coords[key] = value
        if isinstance(key, slice):
            self.coords[key] = value

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.coords[key]
        if isinstance(key, slice):
            return tuple(self.coords[key])


v = RadiusVector(1, 1, 1, 1)
print(v[1])  # 1
v[:] = 1, 2, 3, 4
print(v[2])  # 3
print(v[1:])  # (2, 3, 4)
v[0] = 10.5
print(v[0])
v[1::2] = [9, 7]
print(v.coords)
