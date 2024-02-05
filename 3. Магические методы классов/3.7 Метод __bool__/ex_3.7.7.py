class Ellipse(object):
    """docstring for Ellipse."""

    def __init__(self, *args):
        super(Ellipse, self).__init__()
        if len(args) == 4:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return (
            True
            if hasattr(self, "x1")
            and hasattr(self, "y1")
            and hasattr(self, "x2")
            and hasattr(self, "y2")
            else False
        )

    def get_coords(self):
        if not self:
            raise AttributeError("нет координат для извлечения")
        else:
            return (self.x1, self.y1, self.x2, self.y2)


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 5, 9), Ellipse(2, 6, 8, 45)]

for ellipse in lst_geom:
    if ellipse:
        ellipse.get_coords()
