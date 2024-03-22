class Validator(object):
    """docstring for Validator."""
    def __init__(self, min_value, max_value):
        super(Validator, self).__init__()
        self._min_value = min_value
        self._max_value = max_value


class FloatValidator(Validator):
    """docstring for FloatValidator."""
    def __init__(self, min_value, max_value):
        super(FloatValidator, self).__init__(min_value, max_value)

    def __call__(self, value):
        if not isinstance(value, float) or self._min_value > value  or self._max_value < value:
            raise ValueError('значение не прошло валидацию')

class IntegerValidator(Validator):
    """docstring for IntegerValidator."""
    def __init__(self, min_value, max_value):
        super(IntegerValidator, self).__init__(min_value, max_value)

    def __call__(self, value):
        if not isinstance(value, int) or self._min_value > value or self._max_value < value or type(value) is bool:
            raise ValueError('значение не прошло валидацию')

def is_valid(lst, validators):
    res_lst = []
    for val in lst:
        for validator in validators:
            try:
                validator(val)
                res_lst.append(val)
            except:
                pass
    return res_lst

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)
        
