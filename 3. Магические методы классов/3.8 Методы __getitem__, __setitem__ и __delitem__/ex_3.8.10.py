class Cell(object):
    """docstring for Cell."""

    def __init__(self, value):
        super(Cell, self).__init__()
        self.value = value


class SparseTable(object):
    """docstring for SparseTable."""

    def __init__(self):
        super(SparseTable, self).__init__()
        self.rows = 0
        self.cols = 0
