class BookStudy(object):
    """docstring for BookStudy."""

    def __init__(self, name, author, year):
        super(BookStudy, self).__init__()
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return True if hash(self) == hash(other) else False


lst_in = [
    "Python; Балакирев С.М.; 2020",
    " Python ООП; Балакирев С.М.; 2021",
    " Python ООП; Балакирев С.М.; 2021",
    "Python; Балакирев С.М.; 2021",
]

lst_bs = [
    BookStudy(b.split(sep=";")[0], b.split(sep=";")[1], int(b.split(sep=";")[2]))
    for b in lst_in
]
unique_books = len(set(lst_bs))
print(unique_books)
