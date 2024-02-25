class StringDigit(str):
    """docstring for StringDigit."""
    __instance = None
    def __new__(cls, arg):
        if not arg.isdigit():
            raise ValueError("в строке должны быть только цифры")
        cls.__instance = super().__new__(cls, arg)
        return cls.__instance

    def __add__(self, other):
        if isinstance(other, str):
            return StringDigit(str(self) + other)

    def __radd__(self, other):
        if isinstance(other, str):
            return StringDigit(other + str(self))

sd = StringDigit("123")
print(sd)       # 123
print("wgq")
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = "789" + sd # StringDigit: 789123456
print(sd)
# sd = sd + "12f" # ValueError
