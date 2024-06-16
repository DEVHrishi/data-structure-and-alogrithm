'''There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.'''

class Solution:
    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)  # Path compression
        return parent[x]
    
    def union(self, x, y, parent, rank):
        rootX = self.find(x, parent)
        rootY = self.find(y, parent)

        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        parent = list(range(n))
        rank = [0] * n

        for u, v in connections:
            self.union(u, v, parent, rank)
        
        # Ensure all nodes point to their root parent to get the correct number of components
        for i in range(n):
            self.find(i, parent)
        
        # Count unique components
        unique_components = len(set(parent))
        
        # Minimum number of moves to connect all components
        return unique_components - 1

