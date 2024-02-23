class SellItem(object):
    """docstring for SellItem."""
    def __init__(self, name, price):
        super(SellItem, self).__init__()
        self.name = name
        self.price = price

class Flat(SellItem):
    """docstring for Flat."""
    def __init__(self, name, price, size, rooms):
        super(Flat, self).__init__(name, price)
        self.size = size
        self.rooms = rooms

class House(SellItem):
    """docstring for House."""
    def __init__(self, name, price, material, square):
        super(House, self).__init__(name, price)
        self.material = material
        self.square = square

class Land(SellItem):
    """docstring for Land."""
    def __init__(self, name, price, square):
        super(Land, self).__init__(name, price)
        self.square = square


class Agency(object):
    """docstring for Agency."""
    def __init__(self, name):
        super(Agency, self).__init__()
        self.name = name
        self.__lst_obj = []

    def add_object(self, obj):
        self.__lst_obj.append(obj)

    def remove_object(self, obj):
        self.__lst_obj.remove(obj)

    def get_objects(self):
        return self.__lst_obj

ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
for obj in ag.get_objects():
    print(obj.name)

lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # выделение списка домов
