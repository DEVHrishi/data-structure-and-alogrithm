'''Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of all vertices j such that there is a directed edge from vertex i to vertex j, with  V  vertices and E  edges, your task is to find any valid topological sorting of the graph.

 

In a topological sort, for every directed edge u -> v,  u must come before v in the ordering.

 

Example 1:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0.
Example 2:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 5, 4, 2, 1, 3, 0.
Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them. If your returned topo sort is correct then the console output will be 1 else 0.

Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).'''

# BFS
from collections import deque
class Solution:
    def bfs(self, V, result, adj, store):
        queue = deque()
        for index in range(V):
            if store[index] == 0:
                queue.append(index)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in adj[node]:
                store[neighbor] -= 1
                if store[neighbor] == 0:
                    queue.append(neighbor)
                    
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        store = [0]*V
        
        for i in range(V):
            for idx in adj[i]:
                store[idx] += 1
        result = []

        self.bfs(V, result, adj, store)
        #Check for cycles
        if len(result) != V:
            return []
        
        return result
    
# DFS
class Solution:
    
    def dfs(self, source, visited, result, adj):
        visited.add(source)
        for neighbor in adj[source]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, result, adj)
        result.append(source)
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        result = []
        visited = set()
        for index in range(V):
            if index not in visited:
                self.dfs(index,visited, result, adj)
                
        return result[::-1]