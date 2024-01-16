class WordString(object):
    def __init__(self, str_in=""):
        self.__string = str_in
        self.lst_words = None

    @property
    def string(self):
        """The string property."""
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    def __len__(self):
        self.lst_words = self.__string.split()
        return len(self.lst_words)

    def __call__(self, indx):
        return self.lst_words[indx]


words = WordString()
words.string = "Curse for Pythonn OOP"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
