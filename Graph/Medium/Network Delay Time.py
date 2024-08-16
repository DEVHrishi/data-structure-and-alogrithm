'''You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1'''

import heapq
from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))
        
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        for edge in times:
            self.add_edge(edge[0], edge[1], edge[2])

        min_heap = [(0, k)]
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        visited = set()

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            for v, weight in self.graph[u]:
                if v not in visited:
                    distance = dist[u] + weight
                    if distance < dist[v]:
                        dist[v] = distance 
                        heapq.heappush(min_heap, (distance, v))
        if len(visited) == n:
            dist = [-1 if d == float('inf') else d for d in dist]
            return max(dist) 
        else:
            return -1