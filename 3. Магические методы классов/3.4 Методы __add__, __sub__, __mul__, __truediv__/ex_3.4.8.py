class Item(object):
    """docstring for item."""

    def __init__(self, name, money):
        super(Item, self).__init__()
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        else:
            return self.money + other

    def __radd__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        else:
            return self.money + other


class Budget(object):
    """docstring for Budget."""

    def __init__(self):
        super(Budget, self).__init__()
        self.items_lst = []

    def add_item(self, item):
        self.items_lst.append(item)

    def remove_item(self, indx):
        self.items_lst.pop(indx)

    def get_items(self):
        return self.items_lst


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x

print(s)
