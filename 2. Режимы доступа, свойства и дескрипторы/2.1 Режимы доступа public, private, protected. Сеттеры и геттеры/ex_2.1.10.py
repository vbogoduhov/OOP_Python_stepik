from string import ascii_letters, digits
import random
CHECK_STR = ascii_letters + digits + "@" + "_" + "."
CHAR_FOR_RANDOM = ascii_letters + digits + "." + "_"
class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None
    @classmethod
    def get_random_email(cls):
        rnd_str = random.choices(CHAR_FOR_RANDOM, k=25)
        res_str = ''.join(rnd_str)
        return res_str+'@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not EmailValidator.__is_email_str(email):
            return False
        else:
            split_email = email.split(sep="@")
            if len(split_email) == 1 or len(split_email) > 2:
                return False
            if len(split_email[0]) > 100 or len(split_email[1]) > 50:
                return False
            if len(set(split_email[0]) - set(CHECK_STR)) != 0 \
                or len(set(split_email[1]) - set(CHECK_STR)) != 0:
                return False
            if len(split_email[1].split(sep=".")) == 1:
                return False
            if email.find("..") != -1:
                return False

            return True


    @staticmethod
    def __is_email_str(email):
        return type(email) is str
