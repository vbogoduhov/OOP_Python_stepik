class StackObj(object):
    """docstring for StackObj."""
    def __init__(self, data=None):
        super(StackObj, self).__init__()
        self.data = data
        self.next = None


class Stack(object):
    """docstring for Stack."""
    def __init__(self):
        super(Stack, self).__init__()
        self.top = None
        self.count = 0

    def pop(self):
        next = self.top
        count = 0
        while next:
            if next.next is None:
                self.count -= 1
                self[count - 1].next = None
                return next
            else:
                count += 1
                next = next.next


    def push(self, obj):
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

    def __check_index(self, indx):
        if (not isinstance(indx, int)) or (0 > indx) or (indx >= self.count):
            raise IndexError('неверный индекс')
        return True

    def __getitem__(self, key):
        if self.__check_index(key):
            if key == 0:
                return self.top
            count = 1
            next = self.top.next
            while next:
                if count == key:
                    return next
                else:
                    next = next.next
                    count += 1
    def __setitem__(self, key, value):
        if self.__check_index(key):
            if key == 0:
                tmp = self.top.next
                self.top = value
                self.top.next = tmp
            else:
                count = 1
                next = self.top.next
                prev = self.top
                while next:
                    if key == count:
                        tmp = next.next
                        next = value
                        next.next = tmp
                        prev.next = next
                        break
                    else:
                        prev = next
                        next = next.next
                        count += 1

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("pig suka"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
print(st[0].data)
print(st.count)
# res = st[3] # исключение IndexError
st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
