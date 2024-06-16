'''You are given an Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

Example1:

Input:
n = 9, m= 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
Output:
0 1 2 1 2 3 3 4 4
Explanation:
Example2:

Input:
n = 4, m= 4
edges=[[0,0],[1,1],[1,3],[3,0]] 
src=3
Output:
1 1 -1 0
Explanation:
Your Task:
You don't need to print or input anything. Complete the function shortest path() which takes a 2d vector or array of edges representing the edges of an undirected graph with unit weight, an integer n as the number of nodes, an integer m as a number of edges and an integer src as the input parameters and returns an integer array or vector, denoting the vector of distance from src to all nodes.'''

from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edges(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)

        
    def bfs(self, source, visited, dist):
        dist[source] = 0
        queue = deque([source])
        visited.add(source)
        
        while queue:
            node = queue.popleft()
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dist[neighbor] = dist[node] + 1
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
    def shortestPath(self, edges, n, m, src):
        # code here
        for edge in edges:
            self.add_edges(edge[0], edge[1])
            
        dist = [-1]*n
        visited = set()
    
        
        self.bfs(src, visited, dist)
        
        return distj