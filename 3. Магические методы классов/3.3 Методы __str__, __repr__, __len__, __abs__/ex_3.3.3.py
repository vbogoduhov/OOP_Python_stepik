class Model(object):
    """Представление объекта модели, для запроса к БД"""

    def query(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self):
        if len(self.__dict__) == 0:
            return "Model"
        else:
            str_out = "Model: " + ", ".join(
                [f"{key} = {value}" for key, value in self.__dict__.items()]
            )
            return str_out


m = Model()
print(m)

m.query(id=1, name="hfhbvq", value=5412, age=55)
print(m)
