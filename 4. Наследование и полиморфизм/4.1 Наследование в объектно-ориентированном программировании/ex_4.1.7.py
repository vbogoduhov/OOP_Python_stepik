class Singleton(object):
    """docstring for Singleton."""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


class Game(Singleton):
    """docstring for Game."""
    def __init__(self, name):
        super(Game, self).__init__()
        if "name" not in self.__dict__:
            self.name = name


g = Game("first Game")
g2 = Game("second Game")
g3 = Game("three Game")
print(g.name, g2.name, g3.name)
# print(Singleton.__count)
