from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    @classmethod
    def check_card_number(cls, number):
        if len(number.split(sep='-')) == 4 and len(set(number.replace('-','')) - set(cls.CHARS_FOR_NAME)) == 0 and len(number) == 19 and number.replace('-', '').isdigit():
            return True
        else:
            return False

    @classmethod
    def check_name(cls, name):
        if len(name.split(sep=' ')) == 2 and len(set(name.replace(' ', '')) - set(cls.CHARS_FOR_NAME)) == 0:
            return True
        else:
            return False

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAkIREV")
print(is_name, is_number)
