from abc import ABC, abstractmethod


class Model(ABC):
    """docstring for Model."""

    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    """docstring for ModelForm."""

    __count = 0

    def __init__(self, login, password):
        super(ModelForm, self).__init__()
        self._login = login
        self._password = password
        ModelForm.__count += 1
        self._id = ModelForm.__count

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())
