class Animal(object):
    """docstring for Animal."""

    def __init__(self, name, old):
        super().__init__()
        self.name = name
        self.old = old

    def __setattr__(self, key, value):
        if key == "name" and isinstance(value, str):
            object.__setattr__(self, key, value)
        if key == "old" and isinstance(value, int):
            object.__setattr__(self, key, value)


class Cat(Animal):
    """docstring for Cat."""

    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def __setattr__(self, key, value):
        if key == "color" and isinstance(value, str):
            object.__setattr__(self, key, value)
        if key == "weight" and isinstance(value, (float, int)) and value > 0:
            object.__setattr__(self, key, value)
        if key in ('name', 'old'):
            super().__setattr__(key, value)

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


class Dog(Animal):
    """docstring for Dog."""

    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def __setattr__(self, key, value):
        if key == "breed" and isinstance(value, str):
            object.__setattr__(self, key, value)
        if (
            key == "size"
            and isinstance(value, tuple)
            and isinstance(value[0], (int, float))
            and isinstance(value[1], (int, float))
            and value[0] > 0
            and value[1] > 0
        ):
            object.__setattr__(self, key, value)
        if key in ('name', 'old'):
            super().__setattr__(key, value)
    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"


cat = Cat("Vaska", 35, "red-white", 15)
dog = Dog("Jack", 44, "Rassel", (12.3, 15.4))

print(cat.get_info())
print(dog.get_info())
