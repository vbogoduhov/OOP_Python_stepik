class Book(object):
    """представление книг"""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


str_in = "Python ООП; Балакирев С.М.; 1024".split(sep=";")
b = Book(str_in[0], str_in[1], str_in[2])
print(b)
