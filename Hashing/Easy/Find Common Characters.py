'''Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]'''

from ast import List
import string


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alphabet = string.ascii_lowercase
        d = {c: 0 for c in alphabet}
        
        for k, v in d.items():
            d[k] = min([word.count(k) for word in A])

        res = []
        for c, n in d.items():
            if n > 0:
                res += [c] * n
        return res

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        count = {}
        for x in A[0]:
            count[x] = count.get(x, 0) + 1
            
        
        for x in count:
            for i in range(1,len(A)):
                if x in A[i]:
                    count[x] = min(count[x], A[i].count(x))
                    
                else:
                    count[x] = 0
                    break
        
        ans = []
        for k,v in count.items():
            ans += v * [k]
        return ans