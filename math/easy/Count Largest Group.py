'''You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.'''

class Solution:
    def countLargestGroup(self, n: int) -> int:

        # This method provides the sum of the digits of a number
        def sumDigits(number: int) -> int:

            return sum([int(d) for d in str(number)])
        
        # We initializate a dictionary to group the number by sumDigits
        freq = {}

        for j in range(1, n+1):

            sumD = sumDigits(j)

            if sumD in freq:
                freq[sumD] += [sumD]
            else: 
                freq[sumD] = [sumD]
        
        # We look at the number of elements with a given digitSum
        groupLenght = [len(val) for val in freq.values()]

        # We return the number of the largest groups
        return groupLenght.count(max(groupLenght))