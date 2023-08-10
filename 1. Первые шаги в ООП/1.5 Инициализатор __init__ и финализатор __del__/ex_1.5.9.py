class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj

in_str = """1. Первые шаги в ООП
1.1 Как правильно проходить этот курс
1.2 Концепция ООП простыми словами
1.3 Классы и объекты. Атрибуты классов и объектов
1.4 Методы классов. Параметр self
1.5 Инициализатор init и финализатор del
1.6 Магический метод new. Пример паттерна Singleton
1.7 Методы класса (classmethod) и статические методы (staticmethod)"""

lst_in = in_str.split(sep="\n")
head_obj = ListObject(lst_in[0])
head = head_obj

for data in lst_in[1:]:
    node = ListObject(data)
    head.link(node)
    head = node

# Далее код для проверки работы
next = head_obj.next_obj
print(head_obj.data)
while next:
    print(next.data)
    next = next.next_obj
