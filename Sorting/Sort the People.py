'''You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.'''

from ast import List

# tc = O(n^2) and sc = O(n)
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        s = sorted(heights, reverse = True)
        l = []
        for i in s:
            x = heights.index(i)
            l.append(names[x])
        return l

# tc = O(nlogn) and sc = O(n)
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        l = zip(names, heights)
        l = sorted(l, key=lambda x: x[1], reverse=True)
        return [i[0] for i in l]