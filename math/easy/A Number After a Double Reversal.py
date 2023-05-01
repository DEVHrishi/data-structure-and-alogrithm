'''Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.'''
# tc = O(n) and sc = (n)
def isSameAfterReversals(self, num: int) -> bool:
        reverse = 0
        reverse2 = 0
        tmp = num
        while num > 0:
            reminder = num %10
            reverse = (reverse *10) + reminder
            num = num //10
        while reverse > 0:
            reminder = reverse %10
            reverse2 = (reverse2 *10) + reminder
            reverse = reverse //10
            
        if tmp == reverse2:
            return True
        return False

# tc = O(n) and sc = (n)
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)[::-1]
        d = int(s)
        k = str(d)[::-1]
        return num == int(k)

def isSameAfterReversals(self, num: int) -> bool:
        return (num == 0) or (num % 10 != 0)
        """
        When num = 526, second condition will be true => (526 % 10) = 6 
        When num = 1800, first and second condition are false => (1800 != 0) or (1800 % 10) = 0 
        When num = 0, first condition will be true => 0 == 0
        """