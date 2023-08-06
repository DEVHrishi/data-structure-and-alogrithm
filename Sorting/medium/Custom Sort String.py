'''You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

 

Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
Example 2:

Input: order = "cbafg", s = "abcd"
Output: "cbad"'''

from collections import Counter
# tc: O(n+m) and sc: O(n)
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        o_count = Counter(order)
        s_count = Counter(s)
        ans = ''
        for i in order:
                ans += (i*s.count(i))
        for i in s:
            if i not in order:
                ans += i
        return ans