'''Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.'''
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            x = arr.count(arr[i])
            if x > n/4:
                return arr[i]

class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return collections.Counter(A).most_common(1)[0][0]
		

from statistics import mode

class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return mode(A)


class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return max(set(A), key = A.count)
		
		
class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return (lambda C: max(C.keys(), key = lambda x: C[x]))(collections.Counter(A))
		