class Dimensions(object):
    """docstring for Dimensions."""
    __instance = None
    def __new__(cls, *args, **kwargs):
        for i in args:
            if i <= 0:
                raise ValueError("габаритные размеры должны быть положительными числами")
        cls.__instance = super().__new__(cls) 
        return cls.__instance

    def __init__(self, a, b,c):
        super(Dimensions, self).__init__()
        self.a = a
        self.b =b
        self.c = c 

    def __setattr__(self, key, value):
        if isinstance(value, (int,float)):
            if value <= 0:
                raise ValueError("габаритные размеры должны быть положительными числами")
            else:
                object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"
lst_dims = [
    Dimensions(float(item.split()[0]),float(item.split()[1]),float(item.split()[2]))
    for item in s_inp.split(sep=";")
]

lst_dims = sorted(lst_dims, key=hash)
for i in lst_dims:
    print(hash(i))
