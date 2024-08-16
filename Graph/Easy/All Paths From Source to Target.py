'''Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]'''

from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.graphh = defaultdict(list)
    
    def add_edge(self, start, end):
        self.graphh[start].append(end)

    def dfs(self, source, temp, result, graph):
        temp += [source]
        if source == len(graph)- 1:
            result.append(list(temp))
            return
        for neighbor in self.graphh[source]:
            self.dfs(neighbor, temp, result, graph)
            temp.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        for index in range(len(graph)):
            for node in graph[index]:
                self.add_edge(index, node)
        result = []
        self.dfs(0,[], result, graph)
        return result

    
    
from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.graphh = defaultdict(list)
    
    def add_edge(self, start, end):
        self.graphh[start].append(end)

    def bfs(self, source, result, graph):
        queue = deque([(source, [source])])

        while queue:
            node, temp = queue.popleft()
            if node == len(graph)-1:
                result.append(temp)
            for neighbor in self.graphh[node]:
                queue.append((neighbor, temp+[neighbor]))

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        for index in range(len(graph)):
            for node in graph[index]:
                self.add_edge(index, node)
        result = []
        self.bfs(0, result, graph)
        return result