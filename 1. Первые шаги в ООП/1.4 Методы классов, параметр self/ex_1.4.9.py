import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

lst_in = ['1 Сергей 35 120000',
        '2 Федор 23 12000',
        '3 Иван 13 1200'
        ]
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        for item in data:
            dict_row = {DataBase.FIELDS[key]: value for key, value in enumerate(item.split(sep=' '))}
            DataBase.lst_data.append(dict_row)

    def select(self, a, b):
        if b >= len(DataBase.lst_data):
            return DataBase.lst_data[a:]
        else:
            return DataBase.lst_data[a:b+1]

db = DataBase()
db.insert(lst_in)
print(db.select(0, 3))