class PhoneNumber:
    def __init__(self, number, fio):
        self.fio = fio
        if self.__check_number(number):
            self.number = number

    def __check_number(self, number):
        if type(number) is not int:
            return False
        if len(str(number)) != 11:
            return False

        return True

class PhoneBook:
    def __init__(self):
        self.lst_phone = []

    def add_phone(self, phone):
        self.lst_phone.append(phone)

    def remove_phone(self, indx):
        self.lst_phone.pop(indx)

    def get_phone_list(self):
        return self.lst_phone