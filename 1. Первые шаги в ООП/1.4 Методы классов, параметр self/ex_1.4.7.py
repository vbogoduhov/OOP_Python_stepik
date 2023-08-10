import sys

class StreamData:

    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            for ind, val in enumerate(lst_values):
                setattr(self, fields[ind], val)
            return True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        # lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        lst_in = [10, 'Питон - основы мастерства', 512] # мы формируем список вручную, в остально нет отличий
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()
print(result)