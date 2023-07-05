class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        if indx <= len(self.goods):
            self.goods.pop(indx)

    def get_list(self):
        return [f"{gd.name}: {gd.price}" for gd in self.goods]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('Toshiba', 50000))
cart.add(TV('Samsung', 35000))
cart.add(Table('Hohoho', 15000))
cart.add(Notebook('Asus', 55000))
cart.add(Notebook('Macbook', 150000))
cart.add(Cup('Cupcup', 550))
