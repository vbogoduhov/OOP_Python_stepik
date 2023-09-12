class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None and self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            prev_obj = self.tail
            self.tail = obj
            self.tail.set_prev(prev_obj)
            self.tail.get_prev().set_next(self.tail)

    def remove_obj(self):
        if self.head != self.tail:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail = None
            self.head = None

    def get_data(self):
        next = self.head
        lst_res = []
        while next:
            lst_res.append(next.get_data())
            next = next.get_next()
        return lst_res


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.add_obj(ObjList("данные 4"))
lst.add_obj(ObjList("данные 5"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3', 'данные 4', 'данные 5']
print(res)
lst.remove_obj()
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)
