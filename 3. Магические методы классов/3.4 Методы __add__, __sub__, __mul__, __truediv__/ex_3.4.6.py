class StackObj:
    """Класс, пердставляющий элемент односвязного списка"""

    def __init__(self, data):
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


class Stack:
    """Класс для управления объектами односвязного списка"""

    def __init__(self):
        self.top = None
        self.tail = None

    def push_back(self, obj):
        if self.top is None and self.tail is None:
            self.top = obj
            self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj

    def pop_back(self):
        current = self.top
        while current:
            if current.next != self.tail:
                current = current.next
            else:
                current.next = None
                self.tail = current
                current = None

    def __add__(self, other):
        if isinstance(other, StackObj):
            self.push_back(other)
            return self

    def __iadd__(self, other):
        if isinstance(other, StackObj):
            self.push_back(other)
            return self

    def __mul__(self, other):
        if isinstance(other, list):
            for el in other:
                self.push_back(StackObj(el))
            return self

    def __imul__(self, other):
        if isinstance(other, list):
            for el in other:
                self.push_back(StackObj(el))
            return self


st = Stack()
s1 = StackObj("1")
s2 = StackObj("2")
st.push_back(s1)
st = st + s2
current = st.top

lst_in = ["5", "6", "12", "asddger"]
st *= lst_in
# st += StackObj("3")
while True:
    if current is None:
        break
    print(current.data, sep="\n")
    current = current.next
