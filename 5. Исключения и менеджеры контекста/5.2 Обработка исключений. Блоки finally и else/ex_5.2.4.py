in_text = input()
lst_in = in_text.split()
res_out = None

def check_values(value):
    if value.isdigit():
        try:
            return int(value)
        except ValueError:
            return float(value)
    else:
        if value[0] != '-' and value.find('.') != -1:
            try:
                return float(value)
            except ValueError:
                pass
        if value[0] == '-' and value.find('.') == -1 and value[1:].isdigit():
            try:
                return int(value)
            except ValueError:
                return float(value)
    return value


try:
    val1, val2 = check_values(lst_in[0]), check_values(lst_in[1])
    if isinstance(val1, (float, int)) and isinstance(val2, (int, float)):
        res_out = val1 + val2
    else:
        res_out = str(val1) + str(val2)
finally:
    print(res_out)


