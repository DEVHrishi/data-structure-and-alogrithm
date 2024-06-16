'''There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.'''

from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def bfs(self, source, result):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        for index in range(len(rooms)):
            for edge in rooms[index]:
                self.add_edge(index, edge)
        result = []
        
        self.bfs(0, result)
        return len(result) == len(rooms)
    
    
from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def dfs(self, source, result, visited):
        visited.add(source)
        result.append(source)
        for neighbor in self.graph[source]:
            if neighbor not in visited:
                self.dfs(neighbor, result, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        for index in range(len(rooms)):
            for edge in rooms[index]:
                self.add_edge(index, edge)
        result = []
        visited = set()
        self.dfs(0, result, visited)
        return len(result) == len(rooms)