class Vertex:

    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = set()
        self.degree = 0

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)
        self.degree += 1


class Graph:

    def __init__(self):
        self.vertices = {}
        self.n_vertices = 0

    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)
        self.n_vertices += 1

    def add_edge(self, edge):
        if edge[0] not in self.vertices.keys():
            self.add_vertex(edge[0])
        self.vertices[edge[0]].add_neighbor(edge[1])
        if edge[1] not in self.vertices.keys():
            self.add_vertex(edge[1])
        self.vertices[edge[1]].add_neighbor(edge[0])

    def neighbors(self, vertex):
        return self.vertices[vertex].neighbors

    def sort_by_degree(self):
        self.vertices = dict(sorted(self.vertices.items(), key=lambda v: v[1].degree, reverse=True))


def find_chromatic(graph):
    colors = [None] * len(graph.vertices)

    for v in graph.vertices:
        neighbor_colors = [colors[u-1] for u in graph.neighbors(v)]

        for j in range(graph.n_vertices):
            if j + 1 not in neighbor_colors:
                colors[v-1] = j + 1
                break

    print(max(colors))


if __name__ == "__main__":
    g = Graph()
    while True:
        try:
            edge = input().split()
            edge = list(map(int, edge))
            g.add_edge(edge)
        except:
            break

    g.sort_by_degree()
    find_chromatic(g)
