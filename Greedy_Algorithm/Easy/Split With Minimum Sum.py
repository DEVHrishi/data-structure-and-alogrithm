'''Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

The concatenation of num1 and num2 is a permutation of num.
In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.

Notes:

It is guaranteed that num does not contain any leading zeros.
The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.
 

Example 1:

Input: num = 4325
Output: 59
Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
Example 2:

Input: num = 687
Output: 75
Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal sum of 75.'''


from heapq import heapify, heappop

# tc: O(log n * log n), sc: O(log n)
class Solution:
    def splitNum(self, num: int) -> int:
        l = list(str(num))
        l.sort()
        m, n = '', ''
        for i in range(len(l)):
            if i % 2 == 0:
                m += l[i]
            else:
                n += l[i]
        return (int(m) + int(n))

# tc: O(log n), sc: O(log n)
class Solution:
    def splitNum(self, num: int) -> int:
        hp = [int(i) for i in str(num)]
        heapify(hp)
        
        n1 = ''
        n2 = ''
        
        while hp:
            n1 += str(heappop(hp))
            if hp:
                n2 += str(heappop(hp))
        
        return int(n1) + int(n2)