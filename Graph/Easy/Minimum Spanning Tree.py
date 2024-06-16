'''Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing pairs of integers. Each pair represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.

Example 1:

Input:
3 3
0 1 5
1 2 3
0 2 1

Output:
4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Example 2:

Input:
2 1
0 1 5

Output:
5
Explanation:
Only one Spanning Tree is possible
which has a weight of 5.
 

Your task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function spanningTree() which takes a number of vertices V and an adjacency list adj as input parameters and returns an integer denoting the sum of weights of the edges of the Minimum Spanning Tree. Here adj[i] contains vectors of size 2, where the first integer in that vector denotes the end of the edge and the second integer denotes the edge weight.

Expected Time Complexity: O(ElogV).
Expected Auxiliary Space: O(V2).'''

from collections import defaultdict
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        visited = set()
        sum_value = 0

        min_heap = [(0, 0)]
        
        while min_heap:
            w, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            sum_value += w
            
            for v, weight in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (weight, v))
        return sum_value
    
    
class Solution:
    def prims_algorithm(self, n: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List[Tuple[int, int]]]:
        # Create the adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((weight, v))
            graph[v].append((weight, u))
        
        # Initialize the priority queue with the first vertex (vertex 0)
        min_heap = [(0, 0)]  # (weight, vertex)
        visited = set()
        total_weight = 0
        parent = [-1] * n  # To store the MST path
        mst_edges = []

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_weight += weight
            
            if parent[u] != -1:
                mst_edges.append((parent[u], u))

            # Add all edges connected to the current vertex to the priority queue
            for next_weight, v in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (next_weight, v))
                    parent[v] = u
        
        # Check if all vertices are included in the MST
        if len(visited) == n:
            return total_weight, mst_edges
        else:
            return -1, []  # The graph is not connected
        
        
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

def kruskal(n, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    dsu = DisjointSetUnion(n)
    mst = []
    mst_cost = 0

    for u, v, weight in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
            mst_cost += weight

    return mst, mst_cost