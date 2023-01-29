import random

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

    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, edge):
        if edge[0] not in self.vertices.keys():
            self.add_vertex(edge[0])
        self.vertices[edge[0]].add_neighbor(edge[1])
        if edge[1] not in self.vertices.keys():
            self.add_vertex(edge[1])
        self.vertices[edge[1]].add_neighbor(edge[0])


class MaximalClique:

    def __init__(self, graph):
        self.graph = graph
        self.nodes = set(self.graph.vertices.keys())
        self.k_maximal = {}
        self.BK_pivot()

    def _BK(self, R, P, X):
        if not P and not X:
            if len(R) not in self.k_maximal.keys():
                self.k_maximal[len(R)] = [sorted(R)]
            else:
                self.k_maximal[len(R)].append(sorted(R))
        else:
            new_P = P.union(X)
            u = random.choice(list(new_P))
            for v in P.copy() - self.graph.vertices[u].neighbors:
                union_R = R.union(set([v]))
                intersect_P = P.intersection(self.graph.vertices[v].neighbors)
                intersect_X = X.intersection(self.graph.vertices[v].neighbors)
                self._BK(union_R, intersect_P, intersect_X)
                P = P - set([v])
                X = X.union(set([v]))

    def BK_pivot(self):
        P = self.nodes
        self._BK(set(), P, set())
        self.k_maximal = dict(sorted(self.k_maximal.items(), key=lambda x: x[0]))
        for k, vs in self.k_maximal.items():
            print(k)
            for v in sorted(vs):
                print('{%s}' % ','.join(map(str, v)).strip('[]'))


if __name__ == "__main__":
    g = Graph()
    while True:
        try:
            edge = input().split()
            edge = list(map(int, edge))
            g.add_edge(edge)
        except:
            break

    MaximalClique(g)
