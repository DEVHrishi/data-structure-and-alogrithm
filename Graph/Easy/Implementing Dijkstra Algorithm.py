'''Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is a list of lists containing two integers where the first integer of each list j denotes there is edge between i and j , second integers corresponds to the weight of that  edge . You are given the source vertex S and You to Find the shortest distance of all the vertex's from the source vertex S. You have to return a list of integers denoting shortest distance between each node and Source vertex S.
 

Note: The Graph doesn't contain any negative weight cycle.

 

Example 1:

Input:
V = 2
adj [] = {{{1, 9}}, {{0, 9}}}
S = 0
Output:
0 9
Explanation:

The source vertex is 0. Hence, the shortest 
distance of node 0 is 0 and the shortest 
distance from node 1 is 9.
 

Example 2:

Input:
V = 3, E = 3
adj = {{{1, 1}, {2, 6}}, {{2, 3}, {0, 1}}, {{1, 3}, {0, 6}}}
S = 2
Output:
4 3 0
Explanation:

For nodes 2 to 0, we can follow the path-
2-1-0. This has a distance of 1+3 = 4,
whereas the path 2-0 has a distance of 6. So,
the Shortest path from 2 to 0 is 4.
The shortest distance from 0 to 1 is 1 .
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function dijkstra()  which takes the number of vertices V and an adjacency list adj as input parameters and Source vertex S returns a list of integers, where ith integer denotes the shortest distance of the ith node from the Source node. Here adj[i] contains a list of lists containing two integers where the first integer j denotes that there is an edge between i and j and the second integer w denotes that the weight between edge i and j is w.

 

Expected Time Complexity: O(V2).
Expected Auxiliary Space: O(V2).'''

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def dijkstra(self, n: int, edges: List[List[int]], src: int) -> List[int]:
        graph = defaultdict(list)
        
        # Build the graph
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Priority queue and distance array
        min_heap = [(0, src)]  # (distance, node)
        distances = [float('inf')] * n
        distances[src] = 0
        
        while min_heap:
            current_dist, u = heapq.heappop(min_heap)
            
            if current_dist > distances[u]:
                continue
            
            for v, weight in graph[u]:
                distance = current_dist + weight
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(min_heap, (distance, v))
        
        # Replace 'inf' with -1 to indicate unreachable nodes
        return [dist if dist != float('inf') else -1 for dist in distances]



import heapq
from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))
        
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        for index in range(V):
            for edge in adj[index]:
                self.add_edge(index, edge[0], edge[1])
        #code here
        min_heap = [(0, S)]
        distance = [float('inf')] * V
        distance[S] = 0
        visited = set()
        
        while min_heap:
            current_dist, u = heapq.heappop(min_heap)
        
            if u in visited:
                continue
            visited.add(u)
            
            for v, weight in self.graph[u]:
                if v not in visited:
                    dist = current_dist + weight
                    if dist < distance[v]:
                        distance[v] = dist
                        heapq.heappush(min_heap, (distance[v], v))
                    
        distance = [-1 if d == float('inf') else d for d in distance]
        return distance