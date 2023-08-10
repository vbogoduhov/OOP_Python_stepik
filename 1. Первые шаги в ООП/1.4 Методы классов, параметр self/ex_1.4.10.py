class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add

        if eng in self.tr:
            if rus not in self.tr[eng]:
                self.tr[eng].append(str(rus))
        else:
            self.tr[eng] = [str(rus)]

    def remove(self, eng):
        # здесь продолжайте метод remove
        if eng in self.tr:
            self.tr.pop(eng)

    def translate(self, eng):
        # здесь продолжайте метод translate
        lst_translate = self.tr[eng]
        return lst_translate

tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
tr_list = tr.translate('go')
print(*tr_list)
assert tr.translate('tree')[0] == 'дерево'
tr.add('digits', '1')
tr.add('digits', '2')
assert tr.translate('digits') == ['1', '2']
print(tr.translate('digits'))