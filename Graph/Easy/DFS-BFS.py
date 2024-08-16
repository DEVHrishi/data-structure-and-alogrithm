from collections import defaultdict, deque;

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, start, end):
        self.graph[start].append(end)
    
    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end='->')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs_util(neighbor, visited)
    
    def dfs(self, v):
        visited = set()
        self.dfs_util(v, visited)
        
    def bfs(self, v):
        visited = set()
        queue = deque([v])
        visited.add(v)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end='->')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = Graph()
g.add_edge(0, 1)
g.add_edge(1,2)
g.add_edge(1, 3)

g.dfs(0)
g.bfs(0)
