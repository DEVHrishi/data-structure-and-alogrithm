'''Given an integer number n, return the difference between the product of its digits and the sum of its digits.'''

#TC = O(n) SC = O(n)
def subtractProductAndSum(self, n: int) -> int:
        arr = [int(a) for a in str(n)]
        x = 1
        y = 0
        for i in arr:
            x = x * i
            y = y + i
        return x-y
        
'''
import numpy
class Solution(object):
    def subtractProductAndSum(self, n):
        new = map(int, str(n))
        return  numpy.prod(new) - sum(new)'''