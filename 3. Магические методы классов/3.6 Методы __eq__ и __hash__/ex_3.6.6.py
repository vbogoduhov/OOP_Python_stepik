class ShopItem(object):
    """docstring for ShopItem."""

    def __init__(self, name, weight, price):
        super(ShopItem, self).__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == "name" and isinstance(value, str):
            object.__setattr__(self, key, value)
        if key in ["weight", "price"] and isinstance(value, (int, float)):
            object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [
    "Системный блок: 1500 75890.56",
    "Монитор Samsung: 2000 34000",
    "Клавиатура: 200.44 545",
    "Монитор Samsung: 2000 34000",
]
shop_items = {}
for item in lst_in:

    lst = item.split(sep=":")
    name, weight, price = lst[0], lst[1].split()[0], lst[1].split()[1]
    sh_item = ShopItem(name, float(weight), float(price))
    count = 1
    shop_items[sh_item] = [
        sh_item,
        count if sh_item not in shop_items else shop_items[sh_item][1] + 1,
    ]

print(len(shop_items), list(shop_items.values()), sep="\n")
