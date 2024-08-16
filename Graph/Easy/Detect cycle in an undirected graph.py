'''Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

Example 1:

Input:  
V = 5, E = 5
adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
Output: 1
Explanation: 

1->2->3->4->1 is a cycle.
Example 2:

Input: 
V = 4, E = 2
adj = {{}, {2}, {1, 3}, {2}}
Output: 0
Explanation: 

No cycle in the graph.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not, return 1 if a cycle is present else return 0.

NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is connected.

 

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)

'''

from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, start, end):
        self.graph[start].append(end)
        
    def dfs(self, source, parent, visited):
        visited.add(source)
        for neighbor in self.graph[source]:
            if neighbor not in visited:
                if self.dfs(neighbor, source, visited):
                    return True
            elif neighbor != parent:
                return True
        return False
        
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        for index in range(len(adj)):
            for edge in adj[index]:
                self.add_edge(index, edge)
                
        visited = set()
        for idx in range(V):
            if idx not in visited:
                if self.dfs(idx, -1, visited):
                    return True
        return False