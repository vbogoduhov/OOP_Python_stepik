import math


class PathLines:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.start_x = 0
        self.start_y = 0
        for line in args:
            self.add_line(line)


    def get_path(self):
        if self.heaf is None:
            return []
        else:
            lst_path = []
            next = self.head
            while next:
                lst_path.append(next)
                next = next.next
            return lst_path

    def get_length(self):
        summ_length = 0
        next = self.head
        x = self.start_x
        y = self.start_y
        while next:
            length_line = self.__get_length_line(x, y, next.x, next.y)
            summ_length += length_line
            x = next.x
            y = next.y
            next = next.next
        return summ_length

    def add_line(self, line):
        if self.head is None:
            self.head = line
            self.tail = line
        else:
            prev = self.tail
            self.tail = line
            self.tail.prev = prev
            prev.next = self.tail

    def __get_length_line(self, x0, y0, x1, y1):
        return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__next = None
        self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_obj):
        self.__next = next_obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev_obj):
        self.__prev = prev_obj

