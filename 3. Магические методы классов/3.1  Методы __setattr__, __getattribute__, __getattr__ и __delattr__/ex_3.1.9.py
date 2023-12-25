class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if key in ["MAX_DIMENSION", "MIN_DIMENSION"]:
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено."
            )
        if (isinstance(value, (int, float))) and (
            self.MIN_DIMENSION <= value <= self.MAX_DIMENSION
        ):
            object.__setattr__(self, key, value)


d = Dimensions(10.5, 20.1, 30)
print(
    hasattr(d, "_Dimensions__a"),
    hasattr(d, "_Dimensions__b"),
    hasattr(d, "_Dimensions__c"),
)
d.a = 8
d.b = 15
d.c = 35
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError
print(a, b, c)
print(
    hasattr(d, "_Dimensions__a"),
    hasattr(d, "_Dimensions__b"),
    hasattr(d, "_Dimensions__c"),
)

print(d.__dict__)
d.a = 8
d.b = 10008
d.c = 3

print(d.__dict__)
# TEST-TASK___________________________________
x = Dimensions(10.0, 20, 30)
print(x.__dict__)

# проверка что в классе прописаны объекты свойства a-b-c
assert type(Dimensions.a) is property, "a - не является объектом свойством property"
assert type(Dimensions.b) is property, "b - не является объектом свойством property"
assert type(Dimensions.c) is property, "c - не является объектом свойством property"

# проверка что в объекте класса существуют 3 приватных локальных атрибута
assert (
    "_Dimensions__a" in x.__dict__
    and "_Dimensions__b" in x.__dict__
    and "_Dimensions__c" in x.__dict__
), "атрибуты не являются приватными"
# проверка что данные считываются с приватных атрибутов
assert (
    x.a == 10.0 and x.b == 20 and x.c == 30
), "при обращении к приватным атрибутам значения не получены проверьте объекты свойства"
# проверка что значения являются целым или вещественным числами
assert (
    type(x.a) in (int, float)
    and type(x.b) in (int, float)
    and type(x.c) in (int, float)
), "значения должны быть или целым числом или вещественным"
# проверка на существование атрибутов минимум-максимум
assert hasattr(x, "MIN_DIMENSION"), "не найден атрибут MIN_DIMENSION"
assert hasattr(x, "MAX_DIMENSION"), "не найден атрибут MAX_DIMENSION"

# проверка что значение в диапазоне
x.a = 9
assert (
    x.a == 10.0
), "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"
x.b = -1
assert (
    x.b == 20
), "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"
x.c = 1001
assert (
    x.c == 30
), "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"

# проверка
# С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions.
# При попытке это сделать генерировать исключение:
# raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
try:
    x.MIN_DIMENSION = 0
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError"

try:
    x.MAX_DIMENSION = 0
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError"

assert (
    "MIN_DIMENSION" not in x.__dict__
), "запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions"
assert (
    "MAX_DIMENSION" not in x.__dict__
), "запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions"
print("Прекрасный ответ !")

