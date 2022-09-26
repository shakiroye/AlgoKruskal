class Graph:
    def __init__(self, sommets):
        self.V = sommets
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        total = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, poids in result:
            print("%d - %d: %d" % (u, v, poids))
            total += poids
        print("\nLe poids du graphe minimal est : ",  total)


g = Graph(9)
g.add_edge(2, 8, 1)
g.add_edge(3, 4, 2)
g.add_edge(8, 7, 2)
g.add_edge(0, 1, 4)
g.add_edge(4, 7, 4)
g.add_edge(3, 8, 6)
g.add_edge(4, 5, 7)
g.add_edge(2, 3, 7)
g.add_edge(4, 1, 8)
g.add_edge(0, 2, 8)
g.add_edge(5, 6, 9)
g.add_edge(6, 7, 10)
g.add_edge(2, 1, 11)
g.add_edge(5, 7, 14)
g.kruskal_algo()