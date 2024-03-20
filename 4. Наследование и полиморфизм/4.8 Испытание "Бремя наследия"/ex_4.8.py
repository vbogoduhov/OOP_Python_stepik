import enum
import math
from sre_constants import RANGE_UNI_IGNORE


class Vertex(object):
    """docstring for Vertex."""

    def __init__(self):
        super(Vertex, self).__init__()
        self._links = []

    @property
    def links(self):
        """The links property."""
        return self._links


class Link(object):
    """docstring for Link."""

    def __init__(self, v1, v2, dist=1):
        super(Link, self).__init__()
        self._v1 = v1
        self._v2 = v2
        if self._v2 not in self._v1._links:
            self._v1._links.append(self._v2)
        if self._v1 not in self._v2._links:
            self._v2._links.append(self._v1)
        self._dist = dist

    @property
    def v1(self):
        """The v1 property."""
        return self._v1

    @property
    def v2(self):
        """The v2 property."""
        return self._v2

    @property
    def dist(self):
        """The dist property."""
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def __eq__(self, other):
        return self.v1 in (other.v1, other.v2) and self.v2 in (other.v1, other.v2)


class LinkedGraph(object):
    """docstring for LinkedGraph."""

    def __init__(self):
        super(LinkedGraph, self).__init__()
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def get_dist_vertex(self, from_v, to_v):
        if from_v == to_v:
            return 0
        for link in self._links:
            if (from_v == link._v1 or from_v == link._v2) and (
                to_v == link._v1 or to_v == link._v2
            ):
                return link._dist
        return math.inf

    def __next_vertex(self, viewed, lenght_path):
        min = -1
        max = math.inf
        for key, value in lenght_path.items():
            if value < max and key not in viewed:
                max = value
                min = key
        return min

    def find_path(self, start_v, stop_v):
        matrix = self.__create_matrix()
        weight_link = [math.inf] * len(self._vertex)
        print(matrix)

        viewed_vertex = set()  # Просмотренные вершины
        path = []  # Список результирующий с наименованием вершин и связями между ними
        lenght_path = {v.name: math.inf for v in self._vertex}
        v = start_v.name
        viewed_vertex.add(v)
        lenght_path[v] = 0
        M = [0] * len(self._vertex)
        print(v, viewed_vertex, lenght_path, M, sep="\n")

        while v != -1:
            for ind, val in enumerate(matrix[v]):
                if str(ind+1) not in viewed_vertex:
                    w = lenght_path[v] + val
                    if w < lenght_path[str(ind)]:
                        lenght_path[str(ind)] = w
                        M[ind] = v
            v = self.__next_vertex(viewed_vertex, lenght_path)
            if v != -1:
                viewed_vertex.add(v)
        start = start_v.name
        end = stop_v.name
        P = [int(end)]
        while end != start:
            end = M[P[-1]-1]
            print(f"end = {end}")
            P.append(int(end))
        print(f"М = {M}", f"lenght_path = {lenght_path}")
        print(P)

    def __create_matrix(self):
        len_matrix = len(self._vertex)
        matrix = {v.name: [math.inf] * len_matrix for v in self._vertex}
        # for r in range(1, len_matrix):
        #     matrix[r][0] = self._vertex[r - 1]
        #     matrix[0][r] = self._vertex[r - 1]
        # Создаём матрицу смежности

        for i, v in enumerate(self._vertex):
            for ind, to_v in enumerate(self._vertex):
                dist = self.get_dist_vertex(v, to_v)
                matrix[v.name][ind] = dist
                dist = 0

        # for i in range(1, len(matrix)):
        #     cur_vertex = matrix[i][0]
        #     # print("Текущая точка:", cur_vertex)
        #     for c in range(1, len(matrix[i])):
        #         # print(matrix[0][c])
        #         dist = map_metro.get_dist_vertex(cur_vertex, matrix[0][c])
        #         # print(f"dist = {dist}")
        #         matrix[i][c] = dist
        #         dist = 0
        print("Матрица смежности готова")
        return matrix


class Station(Vertex):
    """docstring for Station."""

    def __init__(self, name):
        super(Station, self).__init__()
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other):
        if isinstance(other, Station):
            return True if self.name == other.name else False


class LinkMetro(Link):
    """docstring for LinkMetro."""

    def __init__(self, v1, v2, dist):
        super(LinkMetro, self).__init__(v1, v2, dist)


# map2 = LinkedGraph()
# v1 = Vertex()
# v2 = Vertex()
# v3 = Vertex()
# v4 = Vertex()
# v5 = Vertex()
#
# map2.add_link(Link(v1, v2))
# map2.add_link(Link(v2, v3))
# map2.add_link(Link(v2, v4))
# map2.add_link(Link(v3, v4))
# map2.add_link(Link(v4, v5))
#
# assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
# assert (
#     len(map2._vertex) == 5
# ), "неверное число вершин в списке _vertex класса LinkedGraph"
#
# map2.add_link(Link(v2, v1))
# assert (
#     len(map2._links) == 5
# ), "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"
#
# path = map2.find_path(v1, v5)
# s = sum([x.dist for x in path[1]])
# assert (
#     s == 3
# ), "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"
#
# assert (
#     issubclass(Station, Vertex) and issubclass(LinkMetro, Link)
# ), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"
#
# map2 = LinkedGraph()
# v1 = Station("1")
# v2 = Station("2")
# v3 = Station("3")
# v4 = Station("4")
# v5 = Station("5")
#
# map2.add_link(LinkMetro(v1, v2, 1))
# map2.add_link(LinkMetro(v2, v3, 2))
# map2.add_link(LinkMetro(v2, v4, 7))
# map2.add_link(LinkMetro(v3, v4, 3))
# map2.add_link(LinkMetro(v4, v5, 1))
#
# assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
# assert (
#     len(map2._vertex) == 5
# ), "неверное число вершин в списке _vertex класса LinkedGraph"
#
# path = map2.find_path(v1, v5)
#
# assert str(path[0]) == "[1, 2, 3, 4, 5]", path[0]
# s = sum([x.dist for x in path[1]])
# assert s == 7, "неверная суммарная длина маршрута для карты метро"
map_metro = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")
v6 = Station("6")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))
map_metro.add_link(LinkMetro(v1, v4, 4))
map_metro.add_link(LinkMetro(v3, v4, 2))
map_metro.add_link(LinkMetro(v2, v5, 5))
map_metro.add_link(LinkMetro(v4, v5, 2))
map_metro.add_link(LinkMetro(v4, v6, 1))
map_metro.add_link(LinkMetro(v5, v6, 4))

map_metro.find_path(v1, v4)
# def create_matrix(lg):
#     len_matrix = len(lg._vertex)
#     matrix = {v.name: [math.inf] * len_matrix for v in lg._vertex}
#     # matrix = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
#     # for r in range(len_matrix):
#     #     matrix[r][0] = lg._vertex[r - 1]
#     #     matrix[0][r] = lg._vertex[r - 1]
#     return matrix
#
#
# def scan_matrix(matrix, map_metro):
#     # for i in range(1, len(matrix)):
#     #     cur_vertex = matrix[i][0]
#     #     print("Текущая точка:", cur_vertex)
#     #     for c in range(1, len(matrix[i])):
#     #         print(matrix[0][c])
#     #         dist = map_metro.get_dist_vertex(cur_vertex, matrix[0][c])
#     #         print(f"dist = {dist}")
#     #         matrix[i][c] = dist
#     #         dist = 0
#     for i, v in enumerate(map_metro._vertex):
#         for ind, to_v in enumerate(map_metro._vertex):
#             dist = map_metro.get_dist_vertex(v, to_v)
#             matrix[v.name][ind] = dist
#             dist = 0
#
#     print("Матрица смежности готова")
#     return matrix
#
#
# print(len(map_metro._vertex))
# for vertex in map_metro._vertex:
#     print(f"vertex -- {vertex.name}")
#     for v in vertex._links:
#         print(f"link to {v.name}")
#
# matrix = create_matrix(map_metro)
# res_matrix = scan_matrix(matrix, map_metro)
# # for r in range(len(res_matrix)):
# #     for c in range(len(res_matrix[r])):
# #         print(res_matrix[r][c], end=" ")
# #     print()
# for key, value in matrix.items():
#     print(f"{key}: {value}")
#
#
# def find_path(matrix, start_v, end_v):
#     pass
