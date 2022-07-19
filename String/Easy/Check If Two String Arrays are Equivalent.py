'''Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.'''

# TC = O(n+m) & SC = O(n+m)
class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        return (''.join(word1)) == (''.join(word2))

# TC = O(min(m,n)) & SC = O(1)
class Solution:
    def arrayStringsAreEqual(self, word1, word2 ) -> bool:
        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1 != c2:
                return False
        return True

    def generate(self, wordlist ):
        for word in wordlist:
            for char in word:
                yield char
        yield None