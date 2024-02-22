class Book(object):
    """docstring for Book."""

    def __init__(self, title, author, pages, year):
        super(Book, self).__init__()
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    """docstring for DigitBook."""

    def __init__(self, title, author, pages, year, size, frm):
        super(DigitBook, self).__init__(title, author, pages, year)
        self.size = size
        self.frm = frm
