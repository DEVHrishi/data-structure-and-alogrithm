'''You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18'''

import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    adj[i].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))

        min_heap = [(0, 0)]
        visited = set()
        cost = 0

        while min_heap:
            c, u = heapq.heappop(min_heap)

            if u in visited:
                continue
            visited.add(u)
            cost += c

            for w, v in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))
        return cost