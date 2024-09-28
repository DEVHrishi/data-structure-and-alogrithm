class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        
    def add_edge(self, start, end):
        self.graph[start].append(end)
    
    def dfs(self, node, receiver, second):
        if second == 0:
            return receiver[node]
        for i in self.graph[node]:
            second -= 1
            self.dfs(i, receiver, second)
    
    def ThrowTheBall(self, receiver, second):
        for i in range(len(receiver)):
            self.add_edge(i+1, receiver[i])
        print(self.graph)
        return self.dfs(1, receiver, second)

l = Graph()
print(l.ThrowTheBall([2, 4, 1, 5, 3], 6))