class MaxPooling(object):
    """docstring for MaxPooling."""

    def __init__(self, step=(2, 2), size=(2, 2)):
        super(MaxPooling, self).__init__()
        self.step = step
        self.size = size

    def _check_matrix(self, matrix):
        row_count = len(matrix)
        for row in matrix:
            if len(row) != row_count:
                return False
            for el_col in row:
                if not isinstance(el_col, (int, float)):
                    return False
        return True

    def _get_max_pooling(self, matrix):
        number_current_row = 0
        razm_matrix = len(matrix)
        step_col = self.step[1]
        step_row = self.step[0]
        size_col = self.size[1]
        size_row = self.size[0]
        pool_lst = []
        while number_current_row < razm_matrix:
            number_current_col = 0
            sq_lst = []
            current_row = matrix[number_current_row]
            while number_current_col < len(current_row):
                tmp_lst = []
                row = 0
                while row < size_col:
                    if (number_current_row + size_row < razm_matrix + 1) and (
                        number_current_col + size_col < len(current_row) + 1
                    ):
                        tmp_lst.append(
                            matrix[number_current_row + row][
                                number_current_col : number_current_col + size_col
                            ]
                        )
                        row += 1
                    else:
                        row += 1
                if len(tmp_lst) == size_row:
                    sq_lst.append(max([max(item) for item in tmp_lst]))
                number_current_col += step_col
            if len(sq_lst) > 0:
                pool_lst.append(sq_lst)
            number_current_row += step_row
        return pool_lst

    def __call__(self, matrix):
        if not self._check_matrix(matrix):
            raise ValueError("Неверный формат для первого параметра matrix.")
        else:
            res_pooling = self._get_max_pooling(matrix)
            return res_pooling


mp = MaxPooling(step=(2, 2), size=(2, 2))
# matrix = [[1, 5, 2], [7, 0, 1], [4, 10, 3]]
matrix = [
    [5, 0, 88, 2, 7, 65],
    [1, 33, 7, 45, 0, 1],
    [54, 8, 2, 38, 22, 7],
    [73, 23, 6, 1, 15, 0],
    [4, 12, 9, 1, 76, 6],
    [0, 15, 10, 8, 11, 78],
]

res = mp(matrix)
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])  # [[6, 8], [9, 7]]
print(res)
