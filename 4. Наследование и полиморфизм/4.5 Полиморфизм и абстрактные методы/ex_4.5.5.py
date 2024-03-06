class Validator(object):
    """docstring for Validator."""

    def _is_valid(self, data):
        raise NotImplementedError("в классе не переопределен метод _is_valid")


class FloatValidator(Validator):
    """docstring for FloatValidator."""

    def __init__(self, min_value, max_value):
        super(FloatValidator, self).__init__()
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data):
        if (
            isinstance(data, float)
            and data >= self._min_value
            and data <= self._max_value
        ):
            return True
        else:
            return False

    def __call__(self, value):
        return self._is_valid(value)


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])

print(res_1, res_2, res_3)
