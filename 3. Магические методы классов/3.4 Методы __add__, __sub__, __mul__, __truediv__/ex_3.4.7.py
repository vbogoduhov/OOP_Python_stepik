class Book(object):
    """docstring for Book."""

    def __init__(self, title, author, year):
        super(Book, self).__init__()
        self.title = title
        self.author = author
        self.year = year


class Lib(object):
    """Class Libreries"""

    def __init__(self):
        super(Lib, self).__init__()
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other_book):
        if isinstance(other_book, Book):
            self.book_list.append(other_book)
            return self

    def __iadd__(self, other_book):
        if isinstance(other_book, Book):
            self.book_list.append(other_book)
            return self

    def __sub__(self, other_book):
        if isinstance(other_book, Book):
            self.book_list.remove(other_book)
        else:
            self.book_list.pop(other_book)
        return self

    def __isub__(self, other_book):
        if isinstance(other_book, Book):
            self.book_list.remove(other_book)
        else:
            self.book_list.pop(other_book)
        return self
