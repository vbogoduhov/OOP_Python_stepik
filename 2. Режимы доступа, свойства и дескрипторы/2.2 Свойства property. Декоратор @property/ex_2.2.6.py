class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def __check_next(self, next_obj):
        return (next_obj is None) or (type(next_obj) is StackObj)


    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_obj):
        if self.__check_next(next_obj):
            self.__next = next_obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev


class Stack:

    def __init__(self):
        self.top = None
        self.__end = None

    def push(self, obj):
        if self.top is None and self.__end is None:
            self.top = obj
            self.__end = obj
        else:
            prev = self.__end
            self.__end = obj
            self.__end.prev = prev
            self.__end.prev.next = self.__end

    def pop(self):
        if self.top != self.__end:
            res = self.__end
            self.__end = self.__end.prev
            self.__end.next = None
            return res
        else:
            res = self.top
            self.__end = None
            self.top = None
            return res

    def get_data(self):
        lst_data = []
        if self.top != None:
            data = self.top.data
            next = self.top.next
            lst_data.append(data)
            while next:
                lst_data.append(next.data)
                next = next.next
            return lst_data
        else:
            return lst_data


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st.pop())
print(st.pop())
res = st.get_data()
print(res)