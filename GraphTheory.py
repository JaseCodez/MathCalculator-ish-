"""
Author: Jason Phan
Another silly program
"""
from GraphTheoryDefinition import Graph, Vertice, Edge


def graph_to_matrix(graph: Graph) -> list[list[int]]:
    graph.sort()
    matrix = []
    for i in range(len(graph.vertices)):
        row = []
        for x in range(len(graph.vertices)):
            if is_an_edge(Edge(graph.vertices[i], graph.vertices[x]), graph.edges):
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


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

        n = 0
        for key in visited:
            n += len(visited[key])
        degree = n

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
            new_edge = Edge(v1, v2)
            if (new_edge.v1 is not new_edge.v2) and not is_an_edge(new_edge, edges):
                new_edges.append(new_edge)
    new_graph.edges = new_edges.copy()
    return new_graph



v1 = Vertice(0, "u")
v2 = Vertice(1, "v")
v3 = Vertice(2, '3')
v4 = Vertice(4, 'k')
v5 = Vertice(5, 'a')
v6 = Vertice(6, 'p')
vertices = [v3, v1, v2, v4]
edges = [Edge(v1, v2), Edge(v2, v3), Edge(v3, v4), Edge(v4, v1)]
g = Graph(vertices, edges)

complement = complement_graph(g)
print(is_connected_graph(complement))
