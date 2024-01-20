class NewList(object):
    """Класс представляющий реализацию метода '-'
    для списка"""
    def __init__(self, in_lst=[]):
        super(NewList, self).__init__()
        self.in_lst = in_lst

    def __sub_lst_from_lst(self, lst_from, lst_sub):
        flag = False
        out_lst = []
        from_copy = lst_from.copy()
        sub_copy = lst_sub.copy()
        for element in from_copy:
            for sub in sub_copy:
                # print(f"Текущие элементы: {element} and {sub}")
                if element == sub and type(element) == type(sub):
                    # print(f"{element} = {sub}")
                    sub_copy.remove(sub)
                    flag = True
                    break
            if flag:
                flag = False
                # break
            else:
                # print(f"Добавляем элемент {element} в выходной список")
                out_lst.append(element)

        return out_lst

    def __sub__(self, other):
        if isinstance(other, NewList):
            other = other.in_lst

        out_lst = self.__sub_lst_from_lst(self.in_lst, other)
        return NewList(out_lst)

    def __rsub__(self, other):
        if isinstance(other, NewList):
            other = other.in_lst

        out_lst = self.__sub_lst_from_lst(other, self.in_lst)

        return NewList(out_lst)

    def __isub__(self, other):
        if isinstance(other, NewList):
            other = other.in_lst
        out_lst = self.__sub_lst_from_lst(self.in_lst, other)

        self.in_lst = out_lst
        return self

    def get_list(self):
        return self.in_lst

lst11 = NewList([1, 5, 4, True, "test", 0, 15])
lst22= NewList([True, "swe", 1, 5])

lst33= lst11 - lst22
print(lst33.in_lst)

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]

print(res_1.in_lst)
print(lst1.in_lst)
print(res_2.in_lst)
print(res_3.in_lst)
print(res_4.in_lst)
print(res_2.get_list())
