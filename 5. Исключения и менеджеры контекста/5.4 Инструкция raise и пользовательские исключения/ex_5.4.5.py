class PrimaryKeyError(Exception):
    """docstring for PrimaryKeyError."""

    def __init__(self, *args, **kwargs):
        super(PrimaryKeyError, self).__init__()
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if len(self.args) == 0 and len(self.kwargs) == 0:
            return "Первичный ключ должен быть целым неотрицательным числом"
        if len(self.kwargs) > 0:
            return f"Значение первичного ключа {list(self.kwargs.keys())[0]} = {self.kwargs[list(self.kwargs.keys())[0]]} недопустимо"


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
