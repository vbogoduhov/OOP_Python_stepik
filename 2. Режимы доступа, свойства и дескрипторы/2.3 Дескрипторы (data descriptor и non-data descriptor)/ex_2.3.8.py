class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if type(string) is not str:
            return False
        if (len(string) < self.min_length) or (len(string) > self.max_length):
            return False
        else:
            return True

class ValidatePrice:
    def __init__(self, max_price):
        self.max_price = max_price

    def validate(self, price):
        if (type(price) in(int, float)) and (0 <= self.max_price <= self.max_price):
            return True

        return False
class StringValue:
    """
    Дескриптор данных
    """
    def __init__(self, validator=ValidateString(2, 50)):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self.name] = value

class PriceValue:
    """
    Дескриптор данных
    """
    def __init__(self, validator=ValidatePrice(10000)):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self.name] = value

class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")