class ShopItem(object):
    """docstring for ShopItem."""

    def __init__(self, name, price, dim):
        super(ShopItem, self).__init__()
        self.name = name
        self.price = price
        self.dim = dim

    def __len__(self):
        return self.dim.a * self.dim.b * self.dim.c


class Dimensions(object):
    """docstring for Dimensions."""

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        super(Dimensions, self).__init__()
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        """The a property."""
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        """The b property."""
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        """The c property."""
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            object.__setattr__(self, key, value)

    def __gt__(self, dim):
        if isinstance(dim, Dimensions):
            return (self.a * self.b * self.c) > (dim.a * dim.b * dim.c)

    def __ge__(self, dim):
        if isinstance(dim, Dimensions):
            return (self.a * self.b * self.c) >= (dim.a * dim.b * dim.c)


lst_shop = [
    ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
    ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
    ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
    ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200)),
]
lst_shop_sorted = sorted(lst_shop, key=len)
for item in lst_shop_sorted:
    print(len(item))
