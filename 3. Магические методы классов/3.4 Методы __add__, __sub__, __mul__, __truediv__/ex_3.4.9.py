class Box3D(object):
    """docstring for Box3D."""

    def __init__(self, width, height, depth):
        super(Box3D, self).__init__()
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, box):
        if isinstance(box, Box3D):
            return Box3D(
                self.width + box.width, self.height + box.height, self.depth + box.depth
            )

    def __mul__(self, box):
        if isinstance(box, (int, float)):
            return Box3D(self.width * box, self.height * box, self.depth * box)

    def __rmul__(self, box):
        if isinstance(box, (int, float)):
            return Box3D(self.width * box, self.height * box, self.depth * box)

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return Box3D(self.width % other, self.height % other, self.depth % other)

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(
                self.width - other.width,
                self.height - other.height,
                self.depth - other.depth,
            )
