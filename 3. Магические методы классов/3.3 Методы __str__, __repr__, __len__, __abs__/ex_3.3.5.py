class ObjList(object):
    """Объект для формирования двусвязного списка"""

    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        """The data property."""
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        """The prev property."""
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        """The next property."""
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList(object):
    """Класс, представляющий двусвязный список"""

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
            self.tail.prev = prev_obj
            self.tail.prev.next = self.tail

    def remove_obj(self, indx):
        if indx == 0:
            if self.head.next is not None:
                self.head.next.prev = None
                self.head = self.head.next
                # self.head.next = None
            else:
                self.head = None
                self.tail = None
        else:
            count = 1
            current_obj = self.head.next
            while current_obj:
                if indx == count:
                    if current_obj.next is not None:
                        current_obj.prev.next = current_obj.next
                        current_obj.next.prev = current_obj.prev
                        current_obj.prev, current_obj.next = None, None
                        break
                    else:
                        current_obj.prev.next = None
                        self.tail = current_obj.prev
                        current_obj.prev = None
                        break
                else:
                    current_obj = current_obj.next
                    count += 1

    def __len__(self):
        next = self.head
        count = 0
        while next:
            next = next.next
            count += 1
        return count

    def __call__(self, indx):
        next = self.head
        count = 0
        while next:
            if count == indx:
                return next.data
            else:
                next = next.next
                count += 1


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))

n = len(linked_lst)  # n = 3
s = linked_lst(1)  # s = Balakirev
print(n, s, linked_lst(2), linked_lst(0))
