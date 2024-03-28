class StringException(Exception):
    """docstring for StringException."""

    def __init__(self, *args):
        super(StringException, self).__init__(args)


class NegativeLengthString(StringException):
    """docstring for NegativeLengthString."""

    def __init__(self, *args):
        super(NegativeLengthString, self).__init__(args)


class ExceedLengthString(StringException):
    """docstring for ExceedLengthString."""

    def __init__(self, *args):
        super(ExceedLengthString, self).__init__(args)


try:
    # здесь команда для генерации исключения
    raise ExceedLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
