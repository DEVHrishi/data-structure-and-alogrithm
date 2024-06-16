'''There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3'''

from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, start, end):
        self.graph[start].append(end)

    def bfs(self, source, visited):
        queue = deque([source])
        visited.add(source)

        while queue:
            node = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # create adjacency list
        for index in range(1, len(isConnected)+1):
            for edge in range(len(isConnected[index-1])):
                if isConnected[index-1][edge] == 1 and index != edge+1:
                    self.add_edge(index, edge+1)
        visited = set()
        count = 0
        for i in range(1, len(isConnected)+1):
            if i not in visited:
                count += 1
                self.bfs(i, visited)

        return count