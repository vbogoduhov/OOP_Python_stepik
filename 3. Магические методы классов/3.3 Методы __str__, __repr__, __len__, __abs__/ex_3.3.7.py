from math import sqrt


class RadiusVector(object):
    """Class RadiusVector."""

    def __init__(self, *args):
        super(RadiusVector, self).__init__()
        if len(args) == 1:
            self.__coords = [0 for _ in range(args[0])]
        else:
            self.__coords = [x for x in args]
        self.__razm = len(args)

    def set_coords(self, *args):
        minrange = min(len(args), len(self.__coords))
        for i in range(minrange):
            self.__coords[i] = args[i]
        self.__razm = len(self.__coords)

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return 0 if self.__razm == 1 else self.__razm

    def __abs__(self):
        if self.__razm > 1:
            summ = sum([x * x for x in self.__coords])
            return sqrt(summ)
        else:
            return 0


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(
    3, -5.6, 8, 10, 11
)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(
    1, 2
)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
print(res_len, res_abs)
