class Book:
    """
    Представление информации о книге
    """
    def __init__(self, *args):
        self.title = args[0] if len(args) > 0 else ""
        self.author = args[1] if len(args) > 0 else ""
        self.pages = args[2] if len(args) > 0 else 0
        self.year = args[3] if len(args) > 0 else 0

    def __setattr__(self, key, value):
        if key in ("title", "author"):
            if type(value) is not str:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        if key in ("pages", "year"):
            if type(value) is not int:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)

book = Book()

book.title = "Python ООП"
book.author = "Сергей Балакирев"
book.pages = 123
book.year = 2022
print(book.__dict__)