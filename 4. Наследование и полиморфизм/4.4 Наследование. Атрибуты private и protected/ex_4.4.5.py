class Animal(object):
    """docstring for Animal."""

    def __init__(self, name, kind, old):
        super(Animal, self).__init__()
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        """The name property."""
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        """The kind property."""
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        """The old property."""
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


animals = [
    Animal("Васька", "дворовый кот", 5),
    Animal("Рекс", "немецкая овчарка", 8),
    Animal("Кеша", "попугай", 3),
]
