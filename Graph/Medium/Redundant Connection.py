'''In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]'''


class Solution:
    def find(self, x , parent):
        print(x)
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
        return parent[x]
    
    def union(self, x, y, parent, rank):
        find_a = self.find(x, parent)
        find_b = self.find(y, parent)

        if find_a != find_b:
            if rank[find_a] > rank[find_b]:
                parent[find_b] = find_a

            elif rank[find_b] > rank[find_a]:
                parent[find_a] = find_b
            else:
                parent[find_b] = find_a
                rank[find_a] += 1

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(i for i in range(n+1))
        rank = [0] * (n+1)
        result = []
        for edge in edges:
            if self.find(edge[0], parent) == self.find(edge[1], parent):
                result.append(edge)
            else:
                self.union(edge[0], edge[1], parent, rank)
        return result[-1]