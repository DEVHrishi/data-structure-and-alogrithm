'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.'''

from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, start, end):
        self.graph[start].append(end)

    def bfs(self, result, store, numCourses):
        queue = deque()
        for i in range(numCourses):
            if store[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                store[neighbor] -= 1
                if store[neighbor] == 0:
                    queue.append(neighbor)


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        store = [0]*numCourses
        for edge in prerequisites:
            self.add_edge(edge[0], edge[1])
            store[edge[1]] += 1
        
        result = []
        self.bfs(result, store, numCourses)

        return len(result) == numCourses