class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)



class Product:
    id = 0

    @classmethod
    def set_id(cls, value):
        cls.id = value

    @classmethod
    def get_id(cls):
        return cls.id

    def __init__(self, name, weight, price):
        self.id = self.get_id() + 1
        self.name = name
        self.weight = weight
        self.price = price

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)

    def __setattr__(self, key, value):
        if key == "id":
            if type(value) is not int:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
                self.set_id(value)
        if key == "name":
            if type(value) is not str:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        if key in ("weight", "price"):
            if (type(value) not in (int, float)) or (value < 0):
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
del book.id


