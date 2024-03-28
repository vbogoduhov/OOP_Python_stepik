from datetime import datetime


class DateError(Exception):
    """docstring for DateError."""


class DateString(object):
    """docstring for DateString."""

    def __init__(self, date_string):
        super(DateString, self).__init__()
        # self.date_string = self.__check_format_date(date_string)
        try:
            self.date_string = datetime.strptime(date_string, "%d.%m.%Y").strftime(
                "%d.%m.%Y"
            )
        except ValueError:
            raise DateError

    def __str__(self):
        return self.date_string


# date_string = input()
date_string = "ab.7.2023"

try:
    date = DateString(date_string)
except DateError:
    print("Неверный формат даты")
else:
    print(date)
