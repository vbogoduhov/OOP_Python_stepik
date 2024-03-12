class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView


class ShopGenericView(object):
    """docstring for ShopGenericView."""

    def __init__(self):
        super(ShopGenericView, self).__init__()

    def __repr__(self):
        return f"\n".join([f"{item[0]}: {item[1]}" for item in self.__dict__.items()])


class ShopUserView(object):
    """docstring for ShopUserView."""

    def __init__(self):
        super(ShopUserView, self).__init__()

    def __str__(self):
        return f"\n".join(
            [
                f"{item[0]}: {item[1]}"
                for item in self.__dict__.items()
                if item[0] != "_id"
            ]
        )


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)
