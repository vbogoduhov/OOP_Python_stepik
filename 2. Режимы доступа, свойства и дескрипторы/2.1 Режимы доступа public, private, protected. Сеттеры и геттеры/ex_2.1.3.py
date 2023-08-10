class Clock:
    def __init__(self, tm):
        self.__time = 0
        self.set_time(tm)

    def __check_time(self, tm):
        return 0 <= tm < 100000 and type(tm) is int

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

clock = Clock(4530)