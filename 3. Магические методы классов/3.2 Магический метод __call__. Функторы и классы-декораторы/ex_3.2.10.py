class InputValues(object):
    """Класс-декоратор"""

    def __init__(self, render):
        self.render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper():
            return self.render(func())

        return wrapper


class RenderDigit(object):
    """docstring for RenderDigit."""

    def __call__(self, parameter_list):
        str_out = parameter_list.split(sep=" ")
        lst_out = [
            int(item)
            if (item.isdigit() and item.find(".") == -1)
            or (item[0] == "-" and item[1:].isdigit())
            else None
            for item in str_out
        ]
        return lst_out


@InputValues(RenderDigit())
def input_dg():
    return input()


res = input_dg()
print(res)
# rnd = RenderDigit()
# print(rnd("15 -652 jhfn541 32.21 adfg 5412"))
