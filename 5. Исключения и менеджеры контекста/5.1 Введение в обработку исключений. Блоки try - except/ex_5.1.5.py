class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __getattr__(self, key):
        try:
            return object.__getattr__(self, key)
        except AttributeError:
            print(f"Атрибут с именем {key} не существует")

pt = Point(1, 2)
print(pt.z)
