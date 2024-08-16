'''Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input:


Output: 0
Explanation: no cycle in the graph

Your task:
You dont need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list adj as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.
In the adjacency list adj, element adj[i][j] represents an edge from i to j.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)'''

from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, start, end):
        self.graph[start].append(end)
    
    def dfs(self, node, visited, recStack):
        visited.add(node)
        recStack.add(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.dfs(neighbor, visited, recStack):
                    return True
            elif neighbor in recStack:
                return True
        
        recStack.remove(node)
        return False
    
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        for index in range(len(adj)):
            for edge in adj[index]:
                self.add_edge(index, edge)
                
        visited = set()
        recStack = set()
        
        for idx in range(V):
            if idx not in visited:
                if self.dfs(idx, visited, recStack):
                    return True
        
        return False