"""
Author: Jason Phan
Does some graph stuff
Another silly program
"""
from GraphTheoryDefinition import Graph, Vertice, Edge, WeightedEdge
from typing import Any, Optional, Union
from math import inf


def graph_to_matrix(graph: Graph) -> list[list[int]]:
    graph.sort()
    matrix = []
    for i in range(len(graph.vertices)):
        row = []
        for x in range(len(graph.vertices)):
            if is_an_edge(Edge(graph.vertices[i].clone(), graph.vertices[x].clone()), graph.edges):
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def matrix_to_graph(matrix: list[list[int]]) -> Graph:
    vertices = []
    for i in range(len(matrix)):
        vertices.append(Vertice(i, "v" + str(i + 1)))

    edges = []
    for i in range(len(matrix)):
        # Since the matrix is symmetric
        # we only need to look at the upper triangle
        for x in range(len(matrix[i][i:])):

            if matrix[i][i:][x] == 1:
                edges.append(Edge(vertices[i].clone(), vertices[x + i].clone()))
    return Graph(vertices, edges)


def is_an_edge(e: Edge, edges: list[Edge]) -> bool:
    for edge in edges:
        if e == edge:
            return True
    return False


def exist_a_path(start: Vertice, end: Vertice, graph: Graph) -> bool:
    if start is end:
        return True

    # populate visited dictionary with vertices
    visited = {}
    for vertice in graph.vertices:
        visited[vertice.index] = []

    # things
    degree = 0
    degree_sum = graph.degree_sum()
    other_vert = start
    while degree != degree_sum:
        for edge in graph.edges:
            if (edge.v1 == start and edge.v2 == end) or (edge.v2 == start and edge.v1 == end):
                return True
            elif other_vert.index == edge.v1.index:
                visited[other_vert.index].append(edge)
                visited[edge.v2.index].append(edge)
                if edge.v2.index == end.index:
                    return True
                other_vert = edge.v2

            elif other_vert.index == edge.v2.index:
                visited[other_vert.index].append(edge)
                visited[edge.v1.index].append(edge)
                if edge.v1.index == end.index:
                    return True
                other_vert = edge.v1
            elif other_vert.index == edge.v1.index and other_vert.degree == len(visited[other_vert.index]):
                return False

        degree = 0
        for key in visited:
            degree += len(visited[key])

    return False


def vertice_degree(v1: Vertice, graph: Graph) -> int:
    count = 0
    for edge in graph.edges:
        if v1.index == edge.v1.index or v1.index == edge.v2.index:
            count += 1
    return count


def is_connected_graph(graph: Graph) -> bool:
    for v1 in graph.vertices:
        for v2 in graph.vertices:
            if not exist_a_path(v1, v2, graph):
                return False
    return True


def complement_graph(graph: Graph) -> Graph:
    new_graph = Graph(graph.vertices.copy(), [])
    new_edges = []
    for v1 in graph.vertices:
        for v2 in graph.vertices:
            new_edge = Edge(v1.clone(), v2.clone())
            if (new_edge.v1 is not new_edge.v2) and not is_an_edge(new_edge, edges):
                new_edges.append(new_edge)
    new_graph.edges = new_edges.copy()
    return new_graph


def is_euclidean(graph: Graph) -> bool:
    for vertice in graph.vertices:
        if vertice.degree % 2 != 0:
            return False
    return is_connected_graph(graph)


def is_subgraph(sub: Graph, parent: Graph) -> bool:
    for v in sub.vertices:
        if not is_a_vertice(v, parent.vertices):
            return False
    for edge in sub.edges:
        if not is_an_edge(edge, parent.edges):
            return False
    return True


def is_a_vertice(vertice: Vertice, vertices: list[Vertice]) -> bool:
    for v in vertices:
        if vertice == v:
            return True
    return False


def is_simple_graph(graph: Graph) -> bool:
    lst = []
    for edge in graph.edges:
        if edge.v1.index == edge.v2.index:
            return False
        if not is_an_edge(edge, lst):
            lst.append(edge)
        else:
            return False
    return True


def is_a_K_graph(graph: Graph) -> bool:
    return len(complement_graph(graph).edges) == 0


def is_cycle_graph(graph: Graph) -> bool:
    for vertice in graph.vertices:
        if vertice.degree != 2: 
            return False
    return is_connected_graph(graph)


def is_bipartite(graph: Graph) -> bool:
    pass


def jason_shortest_path_algorithm(start: Vertice, end: Vertice, graph: Graph) -> tuple[str, int]:
    """
    Assuming that start and end are vertices in graph, and there exist a path from start to end.
    This function is recursive.
    :param start:
    :param end:
    :param graph:
    :return:
    """
    # Base Case
    temp = get_edge_in_edges(start, end, graph)
    if temp is not None:
        return temp.v1.name + "-" + temp.v2.name, temp.weight
    # Recursive Case
    shortest = ('', inf)
    for vertice in graph.vertices:
        temp = get_edge_in_edges(start, vertice, graph)

        recursive = None
        if temp is not None and temp.v1.index == start.index:
            graph.edges.remove(temp)
            recursive = jason_shortest_path_algorithm(temp.v2, end, graph)

        elif temp is not None and temp.v2.index == start.index:
            graph.edges.remove(temp)
            recursive = jason_shortest_path_algorithm(temp.v1, end, graph)

        if recursive is not None and temp is not None:
            graph.edges.append(temp)
            if shortest[1] > recursive[1] + temp.weight:
                shortest = start.name + "-" + recursive[0], recursive[1] + temp.weight

    return shortest


def get_edge_in_edges(v1: Vertice, v2: Vertice, graph: Graph) -> Union[Edge, WeightedEdge]:
    for edge in graph.edges:
        if Edge(v1.clone(), v2.clone()) == edge:
            return edge
    return None


if __name__ == '__main__':
    v1 = Vertice(0, "v1")
    v2 = Vertice(1, "v2")
    v3 = Vertice(2, 'v3')
    v4 = Vertice(3, 'v4')
    vertices = [v1, v2, v3, v4]
    edges = [WeightedEdge(v1, v2, 1), WeightedEdge(v4, v2, 10),
             WeightedEdge(v1, v3, 4), WeightedEdge(v4, v3, 3)]
    g1 = Graph(vertices, edges)

    print(jason_shortest_path_algorithm(v1, v4, g1))
