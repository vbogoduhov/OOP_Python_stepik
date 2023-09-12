class TreeObj:
    """
    Для описания вершин и листьев решающего дерева
    """
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right



class DecisionTree:
    """
    Для работы с решающим деревом в целом
    """
    __head = None
    __tail = None
    @classmethod
    def predict(cls, root, x):
        cur_obj = root
        while not cur_obj.value:
            if x[cur_obj.indx]:
                cur_obj = cur_obj.left
            else:
                cur_obj = cur_obj.right
        # value = None
        #
        # for ind, val in enumerate(x):
        #     if val == 1:
        #         if cur_obj.left is None and cur_obj.right is None:
        #             value = cur_obj.value
        #         else:
        #             cur_obj = cur_obj.left
        #     else:
        #         if cur_obj.left is None and cur_obj.right is None:
        #             value = cur_obj.value
        #         else:
        #             cur_obj = cur_obj.right

        return cur_obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node is None:
            DecisionTree.__head = obj
        else:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

x = [0, 1, 1]
res = DecisionTree.predict(root, x) # будет программистом
print(res)