class StackObj(object):
    """docstring for StackObj."""

    def __init__(self, data):
        super(StackObj, self).__init__()
        self.__data = data
        self.__next = None

    @property
    def data(self):
        """The data property."""
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        """The next property."""
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack(object):
    """docstring for Stack."""

    def __init__(self):
        super(Stack, self).__init__()
        self.count = 0
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
            self.count += 1
        else:
            if self.top.next is None:
                self.top.next = obj
                self.count += 1
            else:
                next = self.top.next
                while next:
                    if next.next is None:
                        next.next = obj
                        self.count += 1
                        break
                    else:
                        next = next.next

    def push_front(self, obj):
        if self.top is None:
            self.top = obj
            self.count += 1
        else:
            tmp_obj = self.top
            self.top = obj
            self.top.next = tmp_obj
            self.count += 1

    def __iter__(self):
        self.index = self.top
        return self

    def __next__(self):
        if self.index:
            obj = self.index
            self.index = self.index.next
            return obj
        else:
            raise StopIteration

    def __getitem__(self, key):
        if self.__check_index(key):
            if key == 0:
                return self.top.data
            count = 1
            next = self.top.next
            while next:
                if count == key:
                    return next.data
                else:
                    next = next.next
                    count += 1

    def __setitem__(self, key, value):
        if self.__check_index(key):
            if key == 0:
                self.top.data = value
            else:
                count = 1
                next = self.top.next
                while next:
                    if key == count:
                        next.data = value
                        break
                    else:
                        next = next.next
                        count += 1

    def __check_index(self, indx):
        if (not isinstance(indx, int)) or (0 > indx) or (indx >= self.count):
            raise IndexError("неверный индекс")
        return True


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert (
    st[0] == "2" and st[1] == "1"
), "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert (
    st[0] == "0"
), "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(
        obj, StackObj
    ), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
