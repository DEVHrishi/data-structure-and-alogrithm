'''Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"'''

# tc = O(n) and sc = O(2*n)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        def helper(org=s):
            nonlocal ans
            n = 2*k
            if len(org)<k:
                ans += org[::-1]
                return
            else:
                while len(org) > k:
                    t = org[0:n]
                    org = org[n:]
                    x = t[0:k]
                    t = t[k:]
                    ans += x[::-1] + t
                if len(org) <=k:
                    ans += org[::-1]
            return
        helper()
        return ans

# tc = O(n) and sc = O(n)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert the string to a list of characters
        lst = list(s)
        
        # Reverse substrings of length k every 2k characters
        for i in range(0, len(lst), 2*k):
            lst[i:i+k] = reversed(lst[i:i+k])
        
        # Convert the list back to a string and return it
        return "".join(lst)

