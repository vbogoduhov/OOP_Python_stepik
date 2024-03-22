from enum import Flag


s = "1 -5.6 True abc 0 23.56 hello []"
# s = "hello 1 world -2 4.5 True"

lst_in = s.split()


def convert_value(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except:
            return value


lst_out = list(map(convert_value, lst_in))

print(lst_out)
