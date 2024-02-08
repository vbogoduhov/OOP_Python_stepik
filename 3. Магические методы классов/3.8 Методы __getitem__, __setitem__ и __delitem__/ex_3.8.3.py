class Track(object):
    """docstring for Track."""

    def __init__(self, start_x, start_y):
        super(Track, self).__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.lst_point = []

    def add_point(self, x, y, speed):
        self.lst_point.append([(x, y), speed])

    def __chech_index(self, ind):
        if not ind in range(len(self.lst_point)):
            raise IndexError("некорректный индекс")
        else:
            return True

    def __setitem__(self, key, speed):
        if self.__chech_index(key):
            self.lst_point[key][1] = speed

    def __getitem__(self, key):
        if self.__chech_index(key):
            return self.lst_point[key][0], self.lst_point[key][1]
