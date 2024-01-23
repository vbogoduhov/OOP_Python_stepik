from nt import spawnve


class ListMath:
    def __init__(self, lst=[]):
        self.lst_math = lst

    def __setattr__(self, key, value):
        if isinstance(value, list):
            t_lst = [
                i
                for i in value
                if isinstance(i, (int, float)) and not isinstance(i, bool)
            ]
            object.__setattr__(self, key, t_lst)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            out_lst = [other + i for i in self.lst_math]

            return ListMath(out_lst)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            out_lst = [i - other for i in self.lst_math]

            return ListMath(out_lst)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            out_lst = [other * i for i in self.lst_math]

            return ListMath(out_lst)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            out_lst = [i / other for i in self.lst_math]

            return ListMath(out_lst)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            out_lst = [i + other for i in self.lst_math]

            return ListMath(out_lst)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            out_lst = [other - i for i in self.lst_math]

            return ListMath(out_lst)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            out_lst = [other * i for i in self.lst_math]

            return ListMath(out_lst)

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            out_lst = [other / i for i in self.lst_math]

            return ListMath(out_lst)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.lst_math = [i + other for i in self.lst_math]

            return self

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.lst_math = [i - other for i in self.lst_math]

            return self

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.lst_math = [i * other for i in self.lst_math]

            return self

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self.lst_math = [i / other for i in self.lst_math]

            return self


# l = ListMath([1, 5, 15, 32, 12.2, "qgbqer"])
# print(l.lst_math)
# l2 = 15 + l
# l3 = l + 32
# print(l2.lst_math, l3.lst_math, sep="\n")
#
# lst = ListMath([4, 5, 8, 15, 16, 6.6, "str"])
# lstadd = lst + 10  # [14, 15, 18, 25, 26, 16.6]
# lstsub = lst - 2  # [2,3,6,13,14,4.6]
# lstmul = lst * 10  # [40,50,80,150,160,66]
# lstdiv = lst / 2  # [2,2.5,4,7.5,8,3.3]
# # print(lstadd.lst_math, lstsub.lst_math, lstmul.lst_math, lstdiv.lst_math, sep="\n")
# assert lstadd.lst_math == [14, 15, 18, 25, 26, 16.6], "Error in add"
# assert lstsub.lst_math == [2, 3, 6, 13, 14, 4.6], "Error in sub"
# assert lstmul.lst_math == [40, 50, 80, 150, 160, 66], "Error in mul"
# assert lstdiv.lst_math == [2, 2.5, 4, 7.5, 8, 3.3], "Error in div"
# radd = 5 + lst  # [9,10,13,20,21,11.6]
# rsub = 10 - lst  # [6,5,2,-5,-6,3.4]
# rmul = 10 * lst  # [40,50,80,150,160,66]
# rdiv = 100 / lst
# assert radd.lst_math == [9, 10, 13, 20, 21, 11.6], "Error in radd"
# print(rsub.lst_math)
# assert rsub.lst_math == [6, 5, 2, -5, -6, 3.4], "Error in rsub"
# assert rmul.lst_math == [40, 50, 80, 150, 160, 66], "Error in mul"
# assert rdiv.lst_math == [100 / i for i in lst.lst_math], "Error in rdiv"
lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(
    lst3.lst_math
), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [
    1,
    2,
    -5,
    7,
], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [
    77,
    78,
    71,
    83,
], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [
    7,
    6,
    5,
], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [
    -3,
    -2,
    -1,
], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [
    3,
    6,
    9,
], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [
    4,
    8,
    12,
], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0
