from __future__ import annotations


class Vertice:
    index: int
    name: str
    degree: int

    def __init__(self, index: int, name: str):
        self.index = index
        self.name = name
        self.degree = 0

    def set_degree(self, degree: int) -> None:
        self.degree = degree

    def add_degree(self, degree: int) -> None:
        self.degree += degree

    def get_degree(self) -> int:
        return self.degree

    def __eq__(self, other):
        return self.index == other.index and self.name == other.name


class Edge:
    v1: Vertice
    v2: Vertice

    def __init__(self, v1: Vertice, v2: Vertice):
        self.v1 = v1
        self.v2 = v2

    def __eq__(self: Edge, other: Edge):
        non_sym = self.v1.index == other.v1.index and self.v2.index == other.v2.index
        sym = self.v2.index == other.v1.index and self.v1.index == other.v2.index
        return non_sym or sym


def merge_sort(lst: list[Vertice]):
    if len(lst) <= 1:
        return lst
    left = lst[len(lst) // 2:]
    right = lst[:len(lst) // 2]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(lst1: list[Vertice], lst2: list[Vertice]) -> list:
    i = 0
    x = 0
    new_lst = []
    while i < len(lst1) and x < len(lst2):
        if lst1[i].index < lst2[x].index :
            new_lst.append(lst1[i])
            i += 1
        else:
            new_lst.append(lst2[x])
            x += 1

    if i < len(lst1):
        return new_lst + lst1[i:]
    elif x < len(lst2):
        return new_lst + lst2[x:]
    return new_lst


class Graph:
    vertices: list[Vertice]
    edges: list[Edge]

    def __init__(self, vertices: list[Vertice], edges: list[Edge]):
        self.vertices = vertices.copy()
        self.edges = edges.copy()
        self._set_degrees()

    def sort(self):
        self.vertices = merge_sort(self.vertices)

    def degree_sum(self) -> int:
        return 2 * len(self.edges)

    def _set_degrees(self) -> None:
        for v in self.vertices:
            for edge in self.edges:
                if v.index == edge.v1.index:
                    v.add_degree(1)
                if v.index == edge.v2.index:
                    v.add_degree(1)



