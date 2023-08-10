class Money:
    def __init__(self, mn):
        self.__money = 0
        self.set_money(mn)

    def __check_money(self, money):
        return 0 <= money and type(money) is int

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.set_money(self.__money + mn.get_money())
