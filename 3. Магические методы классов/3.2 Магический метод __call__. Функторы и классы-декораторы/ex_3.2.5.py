class DigitRetrieve:
    """
    Преобразование данных из строки в числа
    """

    def __call__(self, *args, **kwargs):
        string_integer = args[0]
        if string_integer.isalpha():
            return None
        else:
            if string_integer.isdigit():
                return int(string_integer)
            else:
                if string_integer.find(".") != -1:
                    return None
                else:
                    if string_integer[0] == "-" and string_integer[1:].isdigit():
                        return int(string_integer)
                    else:
                        return None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
