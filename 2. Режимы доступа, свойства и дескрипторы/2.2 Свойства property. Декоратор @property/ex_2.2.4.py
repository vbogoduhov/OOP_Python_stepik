class Car:
    def __init__(self):
        self.__model = None

    @classmethod
    def __check_model(cls, model):
        return (type(model) is str) and (2<=len(model)<=100)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__check_model(model):
            self.__model = model


car = Car()
car.model = "Toyota"
print(car.model)
