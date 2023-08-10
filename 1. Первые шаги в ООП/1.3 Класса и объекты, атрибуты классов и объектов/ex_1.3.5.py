class Car:
    pass
setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__['color'])