'''You are given a graph of n cities numbered from 1 to n. You are given an array connections where connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together. Return the minimum cost to make all cities connected. If it is impossible, return -1.

Example

Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6

Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1'''

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def minimum_cost_to_connect_cities(n, connections):
    dsu = DisjointSetUnion(n + 1)
    connections.sort(key=lambda x: x[2])
    total_cost = 0
    edges_used = 0

    for u, v, cost in connections:
        if dsu.union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                return total_cost

    return -1 if edges_used != n - 1 else total_cost


