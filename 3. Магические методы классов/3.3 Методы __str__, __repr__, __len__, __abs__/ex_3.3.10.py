class PolyLine(object):
    """Класс представляющий полилинию"""

    def __init__(self, *args):
        super(PolyLine, self).__init__()
        self._coords = [*args]

    def add_coord(self, x, y):
        self._coords.append((x, y))

    def remove_coord(self, indx):
        self._coords.pop(indx)

    def get_coords(self):
        return self._coords
