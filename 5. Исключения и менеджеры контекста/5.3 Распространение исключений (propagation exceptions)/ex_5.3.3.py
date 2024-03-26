def input_int_numbers():
    lst_in = list(map(int, input().split()))
    return tuple(lst_in)


while True:
    try:
        out = input_int_numbers()
    except ValueError:
        pass
    else:
        print(*out)
        break
