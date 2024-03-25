def get_loss(w1, w2, w3, w4):
    res = 10 * w1

    try:
        res = res // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        res = res - 5 * w2 * w3 + w4
        return res
