class ShopInterface(object):
    """docstring for ShopInterface."""

    def get_id(self):
        raise NotImplementedError("в классе не переопределен метод get_id")


class ShopItem(ShopInterface):
    """docstring for SjopItem."""

    __count = 0

    def __init__(self, name, weight, price):
        super(ShopItem, self).__init__()
        self._name = name
        self._weight = weight
        self._price = price
        ShopItem.__count += 1
        self.__id = ShopItem.__count

    def get_id(self):
        return self.__id


item1 = ShopItem("имя1", "вес1", "100")
item2 = ShopItem("имя2", "вес2", "200")
print(item1.get_id())
print(item2.get_id())
