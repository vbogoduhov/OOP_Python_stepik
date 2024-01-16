from math import sqrt
class Complex:
    def __init__(self, real, img):
        self._x = real
        self._i = img

    @property
    def real(self):
        return self._x

    @real.setter
    def real(self, value):
        self._x = value

    @property
    def img(self):
        return self._i

    @img.setter
    def img(self, value):
        self._i = value

    def __setattr__(self, key, value):
        if type(value) in (int, float):
            object.__setattr__(self, key, value)
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return sqrt(self._x * self._x + self._i * self._i)

cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(cmp.real, cmp.img, c_abs)